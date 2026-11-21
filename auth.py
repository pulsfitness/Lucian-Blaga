"""Autentificare Google prin Supabase Auth (flux OAuth PKCE), pentru Streamlit.

Cum funcționează:
1. „Conectează-te cu Google” generează un URL de autorizare Supabase cu provider=google și o
   provocare PKCE. Verificatorul PKCE rămâne DOAR pe server (memoria procesului Streamlit),
   asociat unui identificator aleator `lab_state`, valabil 10 minute și folosibil o singură dată.
2. Google → Supabase → aplicația, cu ?code=...&lab_state=... în URL.
3. Aplicația schimbă codul pe o sesiune (access token + refresh token) și o păstrează în
   st.session_state (numai în sesiunea curentă a browserului). Parola Google nu ajunge niciodată
   la aplicație: autentificarea are loc exclusiv pe paginile Google.
4. Tokenul se reîmprospătează automat înainte de expirare; dacă reîmprospătarea eșuează,
   utilizatoarea este deconectată cu un mesaj clar.

Configurare (Streamlit Secrets sau variabile de mediu) – vezi README.md:
    [supabase]
    url = "https://<proiect>.supabase.co"
    anon_key = "<cheia publică anon / publishable>"
    redirect_url = "https://<aplicatia>.streamlit.app"   # sau http://localhost:8501 local
"""
from __future__ import annotations

import os
import secrets
import threading
import time
from dataclasses import dataclass

import streamlit as st

STATE_TTL_SECONDS = 600
REFRESH_MARGIN_SECONDS = 120
SESSION_KEY = "lab_auth"
NOTICE_KEY = "lab_auth_notice"


@dataclass(frozen=True)
class SupabaseConfig:
    url: str
    anon_key: str
    redirect_url: str


def _secret(section: str, key: str) -> str | None:
    try:
        value = st.secrets[section][key]
        return str(value).strip() or None
    except Exception:
        return None


def get_config() -> SupabaseConfig | None:
    """Întoarce configurația Supabase sau None (mod local SQLite).
    LAB_STORAGE=local forțează modul local chiar dacă există secrete."""
    if os.environ.get("LAB_STORAGE", "").lower() == "local":
        return None
    url = _secret("supabase", "url") or os.environ.get("SUPABASE_URL")
    key = _secret("supabase", "anon_key") or os.environ.get("SUPABASE_ANON_KEY") or os.environ.get("SUPABASE_PUBLISHABLE_KEY")
    redirect = _secret("supabase", "redirect_url") or os.environ.get("APP_URL") or "http://localhost:8501"
    if not url or not key:
        return None
    return SupabaseConfig(url=url.rstrip("/"), anon_key=key, redirect_url=redirect.rstrip("/"))


# --------------------------------------------------------------------------- client
class _CaptureStorage:
    """Stocare minimă compatibilă cu supabase-auth; ne permite să citim verificatorul PKCE."""

    def __init__(self):
        self.data: dict[str, str] = {}

    def get_item(self, key):
        return self.data.get(key)

    def set_item(self, key, value):
        self.data[key] = value

    def remove_item(self, key):
        self.data.pop(key, None)


def _client(cfg: SupabaseConfig, access_token: str | None = None, storage=None):
    from supabase import create_client
    from supabase.lib.client_options import SyncClientOptions

    headers = {"Authorization": f"Bearer {access_token}"} if access_token else {}
    options = SyncClientOptions(flow_type="pkce", auto_refresh_token=False, persist_session=False,
                                headers=headers, storage=storage or _CaptureStorage())
    return create_client(cfg.url, cfg.anon_key, options=options)


def data_client(cfg: SupabaseConfig):
    """Client pentru tabele, autorizat cu tokenul utilizatoarei conectate (RLS se aplică)."""
    user = current_user(cfg)
    if not user:
        raise RuntimeError("Nu ești conectată.")
    return _client(cfg, access_token=st.session_state[SESSION_KEY]["access_token"])


# --------------------------------------------------------------------------- PKCE state
@st.cache_resource
def _pending_states() -> tuple[dict, threading.Lock]:
    return {}, threading.Lock()


def _remember_verifier(state: str, verifier: str) -> None:
    store, lock = _pending_states()
    now = time.time()
    with lock:
        for k in [k for k, (_, t) in store.items() if now - t > STATE_TTL_SECONDS]:
            store.pop(k, None)
        store[state] = (verifier, now)


def _take_verifier(state: str | None) -> str | None:
    if not state:
        return None
    store, lock = _pending_states()
    with lock:
        item = store.pop(state, None)
    if not item or time.time() - item[1] > STATE_TTL_SECONDS:
        return None
    return item[0]


def google_login_url(cfg: SupabaseConfig) -> str:
    """Creează (o singură dată pe sesiune) URL-ul de conectare cu Google."""
    cached = st.session_state.get("lab_login_url")
    if cached and time.time() - cached[1] < STATE_TTL_SECONDS - 60:
        return cached[0]
    storage = _CaptureStorage()
    client = _client(cfg, storage=storage)
    state = secrets.token_urlsafe(24)
    redirect = f"{cfg.redirect_url}/?lab_state={state}"
    resp = client.auth.sign_in_with_oauth({
        "provider": "google",
        "options": {"redirect_to": redirect, "query_params": {"prompt": "select_account"}},
    })
    verifier = next((v for k, v in storage.data.items() if k.endswith("-code-verifier")), None)
    if not verifier:
        raise RuntimeError("Nu s-a putut pregăti conectarea securizată (PKCE).")
    _remember_verifier(state, verifier)
    st.session_state["lab_login_url"] = (resp.url, time.time())
    return resp.url


# --------------------------------------------------------------------------- sesiune
def _store_session(session) -> None:
    user = session.user
    meta = getattr(user, "user_metadata", None) or {}
    st.session_state[SESSION_KEY] = {
        "access_token": session.access_token,
        "refresh_token": session.refresh_token,
        "expires_at": int(session.expires_at or (time.time() + (session.expires_in or 3600))),
        "user_id": str(user.id),
        "email": user.email,
        "name": meta.get("full_name") or meta.get("name") or user.email,
    }


def _notice(kind: str, text: str) -> None:
    st.session_state[NOTICE_KEY] = (kind, text)


def pop_notice():
    return st.session_state.pop(NOTICE_KEY, None)


def _friendly(exc: Exception) -> str:
    msg = str(exc).lower()
    if "expired" in msg or "invalid flow state" in msg or "code verifier" in msg or "both auth code" in msg:
        return "Linkul de conectare a expirat sau a fost deja folosit. Apasă din nou „Conectează-te cu Google”."
    if "provider is not enabled" in msg or "unsupported provider" in msg:
        return "Conectarea cu Google nu este activată în proiectul Supabase (Authentication → Providers → Google)."
    if "redirect" in msg:
        return "Adresa de întoarcere nu este permisă în Supabase (Authentication → URL Configuration)."
    if "connect" in msg or "timeout" in msg or "network" in msg:
        return "Serverul de autentificare nu răspunde. Verifică conexiunea la internet și încearcă din nou."
    return "Conectarea nu a reușit. Încearcă din nou; dacă problema persistă, verifică setările Supabase din README."


def handle_oauth_callback(cfg: SupabaseConfig) -> None:
    """Procesează întoarcerea de la Google (?code=…&lab_state=…) sau o eroare (?error=…)."""
    params = st.query_params
    if "error" in params or "error_description" in params:
        desc = params.get("error_description", "") or params.get("error", "")
        if "access_denied" in str(params.get("error", "")):
            _notice("warning", "Conectarea a fost anulată. Poți încerca din nou oricând.")
        else:
            _notice("error", f"Google/Supabase a refuzat conectarea: {desc}")
        params.clear()
        return
    code = params.get("code")
    if not code:
        return
    verifier = _take_verifier(params.get("lab_state"))
    params.clear()  # codul se folosește o singură dată; îl scoatem imediat din bara de adrese
    if not verifier:
        _notice("error", "Linkul de conectare a expirat sau a fost deja folosit. Apasă din nou „Conectează-te cu Google”.")
        return
    try:
        resp = _client(cfg).auth.exchange_code_for_session({"auth_code": code, "code_verifier": verifier})
        if not resp.session:
            raise RuntimeError("sesiune lipsă")
        _store_session(resp.session)
        st.session_state.pop("lab_login_url", None)
        _notice("success", "Te-ai conectat cu Google. Progresul se salvează acum în contul tău.")
    except Exception as exc:  # noqa: BLE001 – afișăm un mesaj prietenos
        _notice("error", _friendly(exc))


def current_user(cfg: SupabaseConfig | None) -> dict | None:
    """Utilizatoarea conectată (cu token valabil) sau None. Reîmprospătează tokenul la nevoie."""
    if cfg is None:
        return None
    auth = st.session_state.get(SESSION_KEY)
    if not auth:
        return None
    if auth["expires_at"] - time.time() > REFRESH_MARGIN_SECONDS:
        return auth
    try:
        resp = _client(cfg).auth.refresh_session(auth["refresh_token"])
        if not resp.session:
            raise RuntimeError("sesiune lipsă")
        _store_session(resp.session)
        return st.session_state[SESSION_KEY]
    except Exception:  # noqa: BLE001
        st.session_state.pop(SESSION_KEY, None)
        _notice("warning", "Sesiunea a expirat. Conectează-te din nou cu Google pentru a continua salvarea online.")
        return None


def logout(cfg: SupabaseConfig) -> None:
    auth = st.session_state.pop(SESSION_KEY, None)
    st.session_state.pop("lab_login_url", None)
    if auth:
        try:  # revocă refresh tokenul pe server (cel mai bine efort)
            client = _client(cfg)
            client.auth.set_session(auth["access_token"], auth["refresh_token"])
            client.auth.sign_out()
        except Exception:  # noqa: BLE001
            pass
    _notice("info", "Te-ai deconectat. Răspunsurile noi nu mai sunt salvate online până te reconectezi.")
