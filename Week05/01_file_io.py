import sys


def main(files):
    """
    Summarizes poems
    """
    try:
        out = open("results.txt", "w")
    except OSError as e:
        print("Can't open results for writing")
        print(e)
        return

    for filename in files:
        try:
            f = open(filename, "r", encoding="utf-8")
        except FileNotFoundError:
            print("Can't open", filename)
            return
        # file object is like zip file, could only run through once. So we
        # need to run a file everytime if we need it.
        # The readline method grabs one line at a time from the file object
        title = f.readline().strip()
        # Read the first line in a file
        # strip takes all the whitespace before and after each line
       
        author = ' '.join(f.readline().strip().split()[1:])
        # Read the second line in a file
        # split() breaks down words into single letters, split()[1:] means
        #  only take letters from index 1

        line_count = 0
        for _line in f:
            line_count += 1
        out.write("Processed poem: \n")
        out.write(f"Title: {title}\n")
        out.write(f"Author: {author}\n")
        out.write(f"Lines: {line_count}\n")
        out.write("\n")


main(sys.argv[1:])

# In terminal, ls Poems/I* means list all files with name starting "I"
# In terminal, ls Poems/*Shelley* means list all files with element "Shelley"
# In terminal, ls Poems/* means list all files in a list.
