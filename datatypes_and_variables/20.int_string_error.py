a = 5
b = "Hello"

try:
    result = a + b
    print(result)
except TypeError as e:
    print("Error:", e)

print("\nExplanation:")
print("Python cannot add an integer and a string directly because they are different data types.")