"""API endpoints."""

def get_users() -> list[dict]:
    return [{"id": 1, "name": "Talha"}, {"id": 2, "name": "Ali"}]

def get_user(uid: int) -> dict | None:
    return next((u for u in get_users() if u["id"] == uid), None)
