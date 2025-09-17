fullname = input("Input your full name: ")
name_break = fullname.rfind(' ')
first_and_middles = fullname[ : name_break]
last = fullname[name_break + 1 : ]

print("Your full name in last-name first format: ")
print(f"{last}, {first_and_middles}")