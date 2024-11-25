
import sys
import os

counter = 0
for line in open("file.txt", "r"):

    # line = input()

    print(len(line))
    print("LINE: " + line)

    counter += 1

print("lines: " + counter)

