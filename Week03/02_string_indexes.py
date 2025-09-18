in_string = "Hello everybody!"

print(f"Your string is {len(in_string)} characters long.")

print(in_string[0])
print(in_string[1])
print(in_string[2])
print(in_string[3])
print(in_string[4])

print(in_string[len(in_string)-1])

# Index syntax above is pretty universal
# Index syntax below is specific to Python

print(in_string[-1])
print(in_string[-2])
print(in_string[-3])

print(in_string[2:8])

print(in_string)

print(in_string[2:12:2])

print(in_string[-1::-1])

print(in_string[::3])

print(in_string[::])

print(in_string[-1::2])

print(f"The first instance of 'ry' appears at position {in_string.find('ry')}")

print(f"The last instance of 'o' appears at position {in_string.rfind('o')}")

print(f"The last instance of 'O' appears at position {in_string.rfind('O')}")
