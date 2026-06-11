from itertools import combinations

def subsets_of_size(items: set[str], size: int) -> list[tuple[str, ...]]:
    return [tuple(combo) for combo in combinations(sorted(items), size)]

result = subsets_of_size({'Amy', 'Bob', 'Cara', 'Dan', 'Eva'}, 3)
