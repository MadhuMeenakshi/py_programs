def list_difference(last_week: list[str], this_week: list[str]) -> list[str]:
    return list(set(this_week) - set(last_week))

result = list_difference(["hide", "seek", "tag"], ["hide", "seek", "jump", "run"])
