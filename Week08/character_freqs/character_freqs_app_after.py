import sys
from char_freqs import CharFreqs


def main(file_name):
    cf = CharFreqs()
    try:
        f = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return
    for line in f:
        # Feed each line to cf
        cf.count_line(line)
    print("\nCharacter counts dictionary:")

    print(cf.char_counts)

    print("Sorted List:")
    print(cf.sorted_counts)

    print("Character freqs dictionary:")
    print(cf.char_freqs)

    print("")


main(sys.argv[1])
