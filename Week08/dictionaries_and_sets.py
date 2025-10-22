my_empty_dictionary = {}

my_fruit_counter = {
    "apples": 3,  # "apples" is key and 3 is an value
    "oranges": 5,  # Only immutable things can be a key.
    "banana": 2,
    "kiwis": 0
}
print(my_fruit_counter["apples"])
# We access the value by key
# just like we access a list element using the index

my_fruit_counter["pears"] = 7
# Add new fruit into the dict
my_fruit_counter["apples"] += 1
# Modify the value of a certain key

print(my_fruit_counter.items())
# It forms a list of tuples with keys and values

print(my_fruit_counter.keys())
print(my_fruit_counter.values())
# The above two also forms a list of elements (keys or values)

# Dictionary is not like list, it is unordered, that's why
# when we add pears, it is in the last one

del my_fruit_counter["apples"]
# This will delete apple key and its' value

# def my_sort_function(an_item):
#     return an_item[1]
# fruits_by_count = sorted(
#     my_fruit_counter.items(),
#     key=my_sort_function,
#     reverse=True
# )

fruits_by_count = sorted(
    my_fruit_counter.items(),
    key=lambda x: x[1],
    reverse=True
)
# sourted(<list>, <key>, <reverse>)
# <key> is a function that takes an item from the list and sorts it
# <reverse> will just reverse the order
print(fruits_by_count)

for fruit in fruits_by_count:
    print(fruit[0], fruit[1])

my_food_type = {
    "vegetables": [],
    "fruits": [],
    "meats": [],
}

my_food_type["fruits"].append("apple")
my_food_type["vegetables"].append("carrots")
my_food_type["fruits"].append("oranges")
my_food_type["fruits"].append("grapes")
my_food_type["fruits"].append("figs")
print(my_food_type["fruits"][2])

for food in my_food_type["fruits"]:
    food = "bubble gum"
    print(food)
print(my_food_type["fruits"])
# This is not the way to change the value in the dict

for (index, food) in enumerate(my_food_type["fruits"]):
    my_food_type["fruits"][index] = "bubble gum"
    print(food, index)
# enumerate() takes a list and returns a list of tuples where the
# first element is the index and the second is the values
print(my_food_type["fruits"])

# for index in range(len(my_food_type["fruits"])):
#     food = my_food_type["fruits"][index]
#     my_food_type["fruits"][index] = "bubble gum"
#     print(food, index)
# same purpose as the above enumerate

my_fruit_set = {"banana", "fig", "apple"}
print(my_fruit_set)
# sets are also unordered, when we print multiple times, the order
# is not fixed


def check_for_fruit(fruit, fruit_set):
    if fruit in fruit_set:
        print(f"We have a fruit {fruit}")
    else:
        print(f"We do not have the {fruit}")


check_for_fruit("banana", my_fruit_set)
check_for_fruit("watermellon", my_fruit_set)
check_for_fruit("fig", my_fruit_set)
# checking one element exists or not, using sets is faster than list
my_fruit_set.remove("fig")
my_fruit_set.add("peach")
check_for_fruit("fig", my_fruit_set)
check_for_fruit("peach", my_fruit_set)

my_empty_set = set()
print(my_empty_set)
my_empty_dictionary = dict()
my_empty_list = list()

my_empty_set.add("bologna")
print(my_empty_set)