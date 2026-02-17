"""Authentication module."""
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    valid = {"admin": hash_password("admin123")}
    return valid.get(username) == hash_password(password)
