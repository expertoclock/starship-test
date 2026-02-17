"""Auth."""
import hashlib
def hash_pw(pw): return hashlib.sha256(pw.encode()).hexdigest()
def auth(u, pw): return {"admin": hash_pw("admin123")}.get(u) == hash_pw(pw)
