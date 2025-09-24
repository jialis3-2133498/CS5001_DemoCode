import sys # Built-in library


# print(sys.argv) 
# # Prints out a list of strings: ["02_triangle.py"]
#In terminal, if we command: python 02_triangle.py my_argument, it will print out ['02_triangle.py', 'my_argument']

def main(height):
    for row in range(1, height+1): # iterate through height
        print('*' * row) # For each row, print * based on number of rows
        # "string" * int means repeat the "string" for int times

main(int(sys.argv[1]))
