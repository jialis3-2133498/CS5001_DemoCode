in_string = "Hello everybody!"
# Space is a character too
print(f"Your string is {len(in_string)} characters long")

for i in range(0, len(in_string)):
    print(in_string[i])

print([in_string[i] for i in range(0, len(in_string))])

print(in_string[len(in_string)-1]) # How to access the last character in a string

# Below codes are unique to python
print(in_string[-1]) # The last character in a string
print(in_string[-2]) # The second last character in a string
print(in_string[:]) # It means slicing the string from index 0 to index last one

print(in_string[2:8]) # Slicing from index 2 to index 7, inclusive for the index 2, exclusive for the index 8

print(in_string[2:12:2]) # Slicing from index 2 to index 12 by stepping 2, Index: 2, 4, 6, 8, 10
print(in_string[-1::-1]) # Slicing from the last character and slice backward 
print(in_string[::3]) # Slicing all characters by stepping 3
print(in_string[-1::2]) # Slicing from the last character and stepping 2. It will only print "!"

print(f"The first instance of 'ry' appears at position {in_string.find('ry')}") # Find the first occurance from the left
print(f"The last instance of 'o' appears at position {in_string.rfind('o')}") # Find the first occurance from the right
print(f"The last instance of 'O' appears at position {in_string.rfind('O')}") # It will return -1, it means meaningless

