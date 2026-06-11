from collections import Counter

def min_bags_for_distinct_colors(marbles: list[str]) -> int:
    counts = Counter(marbles)
    return max(counts.values())

result = min_bags_for_distinct_colors(['red', 'blue', 'red', 'green', 'blue', 'red'])
