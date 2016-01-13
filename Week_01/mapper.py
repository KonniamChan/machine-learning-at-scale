#!/usr/bin/env python
import sys
import re
count = 0
# Command line inputs
findword = sys.argv[1]
filename = sys.argv[2]
regex = re.compile(findword, re.IGNORECASE)

with open (filename, "r") as myfile:
    for line in myfile.readlines():
        if regex.search(line):
            count += 1
print count