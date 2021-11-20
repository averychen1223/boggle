"""
File: boggle.py
Name: Chia-Yu Chen
----------------------------------------
The aim is to create a Python program that plays Boggle. 
The words must be made up of neighboring squares, and you can't use the same square twice in a word.
Words don't need to be in a straight line.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = "dictionary.txt"

# Global variable
WORDS = []  # a list that contains all words in the dictionary


def play(map, r, c, s, found):
    """
    Utilize DFS algorithm to find words in a the given board
    :param map: (list) A list of list to represent the board
    :param r: (int) An int that represents the current row
    :param c: (int) An int that represents the current column
    :param s: (str) A string represents current found string
    :param found: (list) A list to store found strings
    """
    # base case
    if r < 0 or c < 0 or r >= len(map) or c >= len(map):
        return
    if map[r][c] == "":
        return
    if has_prefix(s) == False:
        return
    if s in WORDS and len(s) >= 4 and s not in found:
        found.append(s)
        print("Found: ", s.upper())

    s = s + map[r][c]
    curr = map[r][c]
    map[r][c] = ""
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for dir in dirs:
        new_r = r + dir[0]
        new_c = c + dir[1]
        play(map, new_r, new_c, s, found)

    map[r][c] = curr


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, "r") as f:
        for line in f:
            words = line.split()
            WORDS.append(words[0])


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in WORDS:
        if word.startswith(sub_s):
            return True
    return False


def main():
    """
    Given a 4x4 board, print out all words contained within the board
    """
    # read words from dictionary
    read_dictionary()

    # create a 4x4 board
    map = []
    for row in range(4):
        s = input(str(row + 1) + " row of letters: ")
        s = s.split()
        rows = []
        for ch in s:
            if len(ch) != 1:
                print("Illegal input")
                return
            else:
                rows.append(ch.lower())
        map.append(rows)

    # find words in the given board
    found = []
    for r in range(4):
        for c in range(4):
            play(map, r, c, "", found)

    # print the useful information
    print("There are " + str(len(found)) + " words in total.")


if __name__ == "__main__":
    main()
