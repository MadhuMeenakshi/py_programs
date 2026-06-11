def shallow_copy(d: dict[str, int]) -> dict[str, int]:
    return d.copy()

result = shallow_copy({'p': 2, 'q': 3})
