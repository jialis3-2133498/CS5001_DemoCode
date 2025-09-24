my_string = "Hello for loops"
for my_character in my_string:
    print(f"Character: {my_character}")
print(f"The value of my_character now is: {my_character}")

HOW_HIGH_TO_COUNT = 10
# for i in range(HOW_HIGH_TO_COUNT): # 0 from 9, exclusive
#     print(f"Value: {i}")

for i in range(HOW_HIGH_TO_COUNT+1): # stepping 2
    print(f"Value: {i}")

print(range(10))
print(list(range(10)))