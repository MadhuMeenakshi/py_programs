import copy

def shallow_vs_deep_copy() -> tuple[dict[str, list[int]], dict[str, list[int]], dict[str, list[int]]]:
    nested = {'numbers': [1, 2]}
    shallow = nested.copy()
    deep = copy.deepcopy(nested)
    shallow['numbers'].append(3)
    deep['numbers'].append(4)
    return nested, shallow, deep

result = shallow_vs_deep_copy()
