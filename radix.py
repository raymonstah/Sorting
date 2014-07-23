#!/usr/bin/env/python

# Raymond Ho
# This is radix sort, it groups numbers by their digits.
# From least significant to most significant
# Radix sort takes O(KN) linear time.
# K is the length of the longest number, and N is size of input
# This program only works with positive integers.

import sys

List = []

# Open file, and store all numbers into list.
with open(sys.argv[1], 'r') as f:
    for line in f:
        List.append(int(line))

m = 10 # This is the number to mod by
n = 1  # This is the number to divide by after %

# Loop until the most significant digit has been processed
for _ in range(len(str(max(List)))):
    arrays = [list() for _ in range(10)]
    for i in List:
        tmp = (i % m) / n
        arrays[tmp].append(i)

    # Copy from arrays back to original list
    a = 0
    for b in range(10):
        bucket = arrays[b]
        for each in bucket:
            List[a] = each
            a += 1

    # Increase the multiplier
    n *= 10
    m *= 10

print List

if sorted(List):
    print "List is sorted"
else:
    print "List is not sorted"


