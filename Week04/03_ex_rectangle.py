import sys


def main(height, width):
    for _ in range(height):
        print("*" * width)


main(int(sys.argv[1]), int(sys.argv[2]))

# use _ if we only need to loop through something
# but will not use any variables along with it
