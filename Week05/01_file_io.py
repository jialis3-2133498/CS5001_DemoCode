import sys


def main(files):
    """
    Summarizes poems
    """
    try:
        out = open("results.txt", "a")
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

        line_count = 0
        for _line in f:
            line_count += 1

        out.write("Processed poem: \n")
        out.write(f"Title: {title}\n")
        out.write(f"Author: {author}\n")
        out.write(f"Lines: {line_count}\n")
        out.write("\n")


main(sys.argv[1:])
