import random

def random_binary_string(length: int) -> str:
    return ''.join(random.choice('01') for _ in range(length))

result = random_binary_string(8)
