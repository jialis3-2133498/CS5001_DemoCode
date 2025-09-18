
string_a = "Hello Wiggly World"[:5]
string_b = "Hello Wild World"[:5]

print(string_a)
print(string_b)

# Evaluate string equality
if (string_a == string_b):
    print("These strings are equal")
else:
    print("These strings are NOT equal")

if (string_a is string_b):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

string_a = string_b

if (string_a is string_b):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")


if ("hello" is "hello"):
    print("Yes, hello is hello")

e = "Hello, new string"
f = "Hello, new string"

if (e is f):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

g = e[:3]
h = e[:3]

if (g is h):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

e = "Hello, new string"
f = "Hello, new string"

g = f[:]

if (g is f):
    print("g is IDENTICAL to f")
else:
    print("g is not identical to f")

h = ''.join(f)
print(h)

if (h is f):
    print("h is IDENTICAL to f")
else:
    print("h is not identical to f")
