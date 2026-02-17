"""Input validation."""
import re

def validate_email(email: str) -> bool:
    return bool(re.match(r'^[\w.+-]+@[\w.-]+\.\w{2,}$', email))

def sanitize(data: str) -> str:
    return re.sub(r'[<>&\'"\\]', '', data).strip()
