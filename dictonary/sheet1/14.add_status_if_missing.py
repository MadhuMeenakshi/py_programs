def add_status_if_missing(user: dict[str, str]) -> dict[str, str]:
    user.setdefault('status', 'active')
    return user

result = add_status_if_missing({'name': 'Riya'})
