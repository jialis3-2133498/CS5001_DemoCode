fruits = ["apple", "banana", "cranberry", "durian",
          "etrog", "fig", "guava", "honeydew"]

print(fruits[1:5])
first_letters = [fruit[0] for fruit in fruits]  # List comprehention
print(first_letters)

fruits_copy = [fruit for fruit in fruits]
print(fruits_copy)

my_string = "Hi there I am a string"
words = my_string.split(' ')
print(words)

join_words = "--".join(words)
print(join_words)

my_num_string = "123456789"
my_num_list = [float(element) for element in my_num_string]
print(my_num_list)

list_of_lists = [
    ['a', 'b', 'c', 'd'],
    [1, 2, 3, 4, 5, 6, 7, "Hi there!"],
    ["apple", "banana", "cranberry"]
]
print(len(list_of_lists))

print(list_of_lists[1][7][0])

new_list = []

new_list.append("cheese")
new_list.append("tomato")
new_list.append("egg")
print(new_list)
new_list.append("Milk")

new_list.insert(0, "yogurt")
print(new_list)

more_groceries = ["meat", "potatoes", "juice"]
new_list.extend(more_groceries)
# Use extend to add elements into a list
# If we use append, that means we add a list into a list
print(new_list)

concat = more_groceries + [1, 2, 3]
print(concat)

my_list = [1, 2, 3]
my_list.insert(0, [4, 5, 6])

my_list[0].insert(0, 7)
print(my_list)