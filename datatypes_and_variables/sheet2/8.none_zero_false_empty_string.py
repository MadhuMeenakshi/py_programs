values = [None, 0, False, ""]

for value in values:
    print(value, type(value))

print("\nConditional Tests:")

for value in values:
    if value:
        print(value, "is True")
    else:
        print(repr(value), "is False")

print("\nThey are different objects and types.")