#!/usr/bin/env python3

"""
all_repri.py
Created by Brendan Apfeld on 2017-06-23.
Please feel free to modify as desired.
"""

import re
import os
import sys
import string

DONE = "todo.txt"

letters = list(string.ascii_uppercase)

def main(directory, shift = 1):
    with open(os.path.join(directory, DONE), 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            # see if it has a priority level
            pri_test = re.findall(r'^\(\D\)', line)
            # if so, change according to shift variable
            if len(pri_test) > 0:
                pri = re.findall(r'[A-Z]', pri_test[0])
                pri = pri[0]
                # get position in letters list
                index = [i for i, s in enumerate(letters) if pri in s]
                # find the new priority level
                new_index = index[0] - shift
                # some if logic so we don't go outside the bounds of our letters
                if new_index < 0:
                    new_index = 0
                if new_index > 25:
                    new_index = 25
                new_pri = str('({0})').format(letters[new_index])
                # write in new priority levels
                line = re.sub(r'^\(\D\)', new_pri, line)
            f.write(line)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: all_repri [TODO_DIR] <shift integer>")
        sys.exit(1)

    if os.path.isdir(sys.argv[1]):
        if len(sys.argv) is 3:
            main(sys.argv[1], int(sys.argv[2]))
        else:
            main(sys.argv[1])
    else:
        print("Error: %s is not a directory" % sys.argv[1])
        sys.exit(1)
