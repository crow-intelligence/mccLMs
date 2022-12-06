#!/usr/bin/env python3

with open("data/interim/huwiki_uncased.txt", "w") as outfile:
    with open("data/interim/huwiki.txt", "r") as infile:
        for l in infile:
            outfile.write(l.lower())
print("wiki is ready")
with open("data/interim/oscar_uncased.txt", "w") as outfile:
    with open("data/interim/oscar.txt", "r") as infile:
        for l in infile:
            outfile.write(l.lower())
print("oscar is ready")
