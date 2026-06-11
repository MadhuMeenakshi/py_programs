import random
import string

def random_until_target(target):
    attempts = 0
    length = len(target)
    while True:
        attempts += 1
        candidate = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
        if candidate == target:
            return candidate, attempts

result = random_until_target("abc")  # Randomly generated 'abc' after N attempts
