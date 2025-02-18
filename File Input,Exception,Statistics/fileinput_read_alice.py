print("Program to analyse contents of the file 'alice.txt'")


with open("alice.txt") as book_file:
    # read in the entire contents of the file as a string
    contents = book_file.read()

    # count number of words by splitting the contents into a list of words
    print("Number of words:", len(contents.split()))

    # count number of lines by splitting the contents into a list of lines
    print("Number of lines:", len(contents.splitlines()))

    # How many times does the word "Alice" appear?
    print("Occurrences of 'Alice':", contents.count("Alice"))
