fruits = ["apple", "banana", "cranberry", "durian",
          "etrog", "fig", "guava", "honeydew"]

print(fruits[1:5])

first_letters = [fruit[0] for fruit in fruits]

print(first_letters)

fruits_copy = [fruit for fruit in fruits]

print(fruits_copy)

my_string = "Hi there I'm a string!"

words = my_string.split(' ')
print(words)

join_words = "--".join(words)
print(join_words)

my_num_string = "123456"

my_num_list = [float(element) for element in my_num_string]

print(my_num_list)

list_of_lists = [
    ['a', 'b', 'c', 'd'],
    [1, 2, 3, 4, 5, 6, 7, "hi there!"],
    ["apple", "banana", "cranberry"]
]

print(len(list_of_lists))

print(list_of_lists[1][7][0])


new_list = []
new_list.append("cheese")
new_list.append("tomato")
new_list.append("egg")

print(new_list)
new_list.append("milk")
print(new_list)

new_list.insert(1, "yogurt")
print(new_list)

more_groceries = ["meat", "potatoes", "juice"]

new_list.extend(more_groceries)
print(new_list)

concat = more_groceries + [1, 2, 3]
print(concat)

my_list = [1, 2, 3]
my_list.insert(0, [4, 5, 6])

my_list[0].insert(0, 7)
print(my_list)
