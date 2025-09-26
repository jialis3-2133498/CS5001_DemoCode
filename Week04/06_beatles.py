
band = ["Paul", "Pete", "John", "George"]
instruments = ["Bass", "Drums", "Vocals", "Guitar", "Trombone"]

print(band)
print(len(band))

print(instruments[1])
print(instruments[2:])
print(instruments[1:3])

print(band)

band[1] = "Ringo"

print(band)

my_string = "Hello string"
print(list(my_string))

for member in band:
    print(f"Introducing {member}")

lineup = zip(band, instruments)

print(lineup)
# print(list(lineup))

lineup_list = list(lineup)

print(lineup_list)

for member_inst in lineup_list:
    print(member_inst)

print(lineup_list)

for member_inst in lineup_list:
    print(f"Member: {member_inst[0]}, Instrument: {member_inst[1]}")


lineup1 = zip(range(10), band, instruments, "Beatles")

list_lineup1 = list(lineup1)

print("Lineup1 converted to list: ", list_lineup1)


print(list_lineup1[2])
print(list_lineup1[2][1])
print(list_lineup1[2][1][2])
# print(list_lineup1[2][0][1])

my_tuple = list_lineup1[2]

print(my_tuple)
# Can't do this because Tuples are immutable
# my_tuple[1] = "Todd"
print(my_tuple)

my_tup_of_lists = ([1, 2, 3], "hello")
print(my_tup_of_lists)
my_tup_of_lists[0][0] = 5
print(my_tup_of_lists)
