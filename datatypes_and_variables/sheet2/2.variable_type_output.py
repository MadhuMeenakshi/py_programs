x = 2
y = 2.0
z = "2"
w = x + int(z)
v = str(x) + z

print("x =", x, type(x))
print("y =", y, type(y))
print("z =", z, type(z))
print("w =", w, type(w))
print("v =", v, type(v))

print("\nExplanation:")
print("int(z) converts '2' to integer.")
print("str(x) converts 2 to string before concatenation.")