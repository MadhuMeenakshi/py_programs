def bulk_update(info: dict[str, int]) -> dict[str, int]:
    info.update({'a': 100, 'b': 100})
    return info

result = bulk_update({'a': 10, 'b': 20})
