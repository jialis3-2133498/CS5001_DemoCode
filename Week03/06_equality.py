string_a = "Hello wiggly World"[:5]
string_b = "Hello wild World"[:5]

print(string_a)
print(string_b)

# Evaluate strings equality
if (string_a == string_b):
    print("These strings are equal")
else:
    print("Those strings are Not equal")

# Evaluate strings identity
if (string_a is string_b):
    print("These strings are identical, i.e. The same object")
else:
    print("These strings are two separate objects")

string_a = string_b # Original stirng_a's data was overwritten by the data of string_b, so both variables share the same data. 
if (string_a is string_b):
    print("These strings are identical, i.e. The same object")
else:
    print("These strings are two separate objects")

if ('hello' is 'hello'):
    print("Yes, hello is hello")


e = "Hello, new string"
f = "Hello, new string"
if (e is f):
    print("These strings are identical, i.e. The same object")
else:
    print("These strings are two separate objects")
# In python, when we create two identical strings, python will save memories by assign both variables with the same data. That's why it will return True
# In the beginning, we created two different strings that share same parts. 

g = e[:3]
h = f[:3]
if (g is h):
    print("These strings are identical, i.e. The same object")
else:
    print("These strings are two separate objects")
# The above codes says two strings are separate objects
# Two examples are different because something related to implementation process when there are spaces or other procedures


g = f[:]
if (g is f):
    print("g is identical to f")
else:
    print("g is not identical to f")

h = ''.join(f) # The method to make two objects that share the same values.
print(h)
if (h is f):
    print("h is identical to f")
else:
    print("h is not identical to f")