def sort_pairs_by_float_desc(t: tuple[tuple[str, str], ...]) -> list[tuple[str, str]]:
    return sorted(t, key=lambda pair: float(pair[1]), reverse=True)

result = sort_pairs_by_float_desc((('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'),))
