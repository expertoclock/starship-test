"""API."""
def get_users(): return [{"id": 1, "name": "Talha"}, {"id": 2, "name": "Ali"}]
def get_user(uid): return next((u for u in get_users() if u["id"] == uid), None)
