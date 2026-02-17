"""Validation."""
import re
def validate_email(e): return bool(re.match(r"^[\\w.+-]+@[\\w.-]+\\.\\w{2,}$", e))
def sanitize(d): return re.sub(r"[<>&]", "", d).strip()
