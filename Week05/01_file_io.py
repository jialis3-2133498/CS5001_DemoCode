import sys


def main(files):
    """
    Summarizes poems
    """
    try:
        out = open("results.txt", "w")
    except OSError:
        print("Can't open results for writing")
        return

    for filename in files:
        try:
            f = open(filename, "r", encoding="utf-8")
        except FileNotFoundError:
            print("Can't open", filename)
            return

        # The readLine method grabs one line at a time from the
        # file object
        title = f.readline().strip()

        author = ' '.join(f.readline().strip().split()[1:])

        print(author)


main(sys.argv[1:])
