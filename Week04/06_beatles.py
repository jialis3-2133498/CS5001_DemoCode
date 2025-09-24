band = ["Paul", "Pete", "John", "George"]
instruments = ["Bass", "Drum", "Vocals", "Guitar", "Trombone"]

print(band)
print(len(band))

print(instruments[1])
print(instruments[2:])

print(band)
band[1] = "Ringo"
print(band)

my_string = "Hello String"
print(list(my_string))

for member in band:
    print(f"Introducting {member}")

lineup = zip(band, instruments)  # zip them into a tuple
print(lineup)
# Only print out the file location and file type. zip file can be used to loop
#   through, but not for printing
print(list(lineup))  # Looop zip for the first time

lineup_list = list(lineup)
for member_inst in lineup:
    print(member_inst)
# zip file only can be looped through onece, that is why the for loop does not
#   print out anything.
# If we want to loop a zip file multiple times, we could make a new list
#   variable
for member_inst in lineup_list:
    print(f"Member: {member_inst[0]}, instrument: {member_inst[1]}")
    # for each tuple, the memebr will be in index 0, and
    # instrument will be in index 1
lineup1 = zip(range(10), band, instruments)
list_lineup1 = list(lineup1)
print("Lineup1 coverted to list: ", list(lineup1))
print(list_lineup1[2])
# Access the tuple with index 2 inside the list
print(list_lineup1[2][1])
# Access the string with index 1 inside the tuple
print(list_lineup1[2][1][2])
# Access the letter with index 2 inside the string

my_tuple = list_lineup1[2]
# print(my_tuple)
# my_tuple[1] = "Todd"
print(my_tuple)
my_tup_of_lists = ([1, 2, 3], "hello")
print(my_tup_of_lists)
my_tup_of_lists[0][0] = 5 
# Tuple is immutable, but list is.
# So list inside a tuple is still immutable
print(my_tup_of_lists)
