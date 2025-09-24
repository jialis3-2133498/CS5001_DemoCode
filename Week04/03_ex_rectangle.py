import sys

def main(height, width):
    for i in range(height+1):
        print("*" * width)

main(int(sys.argv[1]), int(sys.argv[2]))