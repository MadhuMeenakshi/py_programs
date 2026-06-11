def factors_frequency(nums: list[int]) -> dict[int, int]:
    freq: dict[int, int] = {}
    for num in nums:
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                freq[i] = freq.get(i, 0) + 1
                other = num // i
                if other != i:
                    freq[other] = freq.get(other, 0) + 1
    return dict(sorted(freq.items()))

result = factors_frequency([10, 15])
