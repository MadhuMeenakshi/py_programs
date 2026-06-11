def count_groups_by_digit_sum(nums: list[int]) -> int:
    groups: dict[int, int] = {}
    for num in nums:
        digit_sum = sum(int(ch) for ch in str(abs(num)))
        groups[digit_sum] = groups.get(digit_sum, 0) + 1
    return max(groups.values())

result = count_groups_by_digit_sum([11, 20, 12, 21, 3])
