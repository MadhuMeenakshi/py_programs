try:
    d = {[1, 2, 3]: "Python"}
except TypeError as e:
    print("Error:", e)

print("\nExplanation:")
print("Lists are mutable and therefore unhashable.")
print("Dictionary keys must be hashable.")