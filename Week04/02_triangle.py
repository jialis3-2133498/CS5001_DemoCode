import sys # Built-in library
# When use sys, have to use terminal to print out the result, instead of using the run botton
# In terminal, the first index will always be the file name, that means in order to pass something in 
#   from users, we need use sys.argv[1] or greater than 1

# print(sys.argv) 
# # Prints out a list of strings: ["02_triangle.py"]
#In terminal, if we command: python 02_triangle.py my_argument, it will print out ['02_triangle.py', 'my_argument']

def main(height):
    for row in range(1, height+1): # iterate through height
        print('*' * row) # For each row, print * based on number of rows
        # "string" * int means repeat the "string" for int times

main(int(sys.argv[1])) 
# In terminal, we input"python 02_triangle.py 5"
# python 02_triangle has index 0
# 5 has index 1
# sys.argv[1]  means in the terminal input, we are looking for the element with the index 1 and pass into the program
# main(int(5)) will initiate the function and treat 5 as the height parameter