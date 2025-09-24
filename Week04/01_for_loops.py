my_string = "Hello for loops!"

for my_character in my_string:
    print(f"Character: {my_character}")

print(f"The value of my_character now is: {my_character}")

HOW_HIGH_TO_COUNT = 10

for i in range(1, HOW_HIGH_TO_COUNT+1):
    print(f"Value: {i}")

print(f"The variable i is now {i}")

for i in range(1, HOW_HIGH_TO_COUNT+1, 2):
    print(f"Value: {i}")

print(range(10))

print(list(range(10)))

# Some other languages' for loops (NOT Python)
# for (i = 0; i < 10; i++) {
#     // do something with i
# }
