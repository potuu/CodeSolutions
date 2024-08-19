# Task

# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

# Input Format

# A single line containing the string S and integer value k separated by a space.

# Constraints
# 0<k<=len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the combinations with their replacements of string  on separate lines.

# Sample Input
# HACK 2

# Sample Output
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
strng, b = input().split()
strng = sorted(strng)
x = list(combinations_with_replacement(strng, int(b)))
[print(''.join(j)) for i in x]
