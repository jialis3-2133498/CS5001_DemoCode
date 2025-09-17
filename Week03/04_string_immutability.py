phrase = "Change is inevitable"

print("Original string:", phrase)
print("Length of the string:", len(phrase))

mutation1 = phrase + " except from vending machines"
print(f"1: {mutation1}")

mutation2 = mutation1.upper()
print(f"2: {mutation2}")

mutation3 = mutation2.replace(" ", "X") # Replace all spaces in a string with "X"
print(f"3: {mutation3}")

print("Length of the Mut 3:", len(mutation3))

mutation4 = mutation3 + "\n"
print(f"4: {mutation4}")

print("Length of the Mut 4", len(mutation4)) # New line will count as an extra index

print("Original string:", phrase)

print(phrase[0])

# phrase[0] = "Z" 
# The above code means strings are immutable. We can not change it 
# Instead, we need to create a new string upon it based on changes whatever we want

print("Original string:", phrase)

phrase = "Zhange is inevitable"

print("New string:", phrase) # Or we can reassign the variable

print("Done!")
