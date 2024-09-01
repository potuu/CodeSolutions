# A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
# For example, according to the conditions described above,
# GOOGLE would have it's logo with the letters G,O,E.

# Input Format
# A single line of input containing the string S.

# Constraints
# 3<len(S)<=10^4
#  has at least  distinct characters

# Output Format
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0
# aabbbccde

# Sample Output 0
# b 3
# a 2
# c 2

# Explanation 0
# Here, b occurs 2 times. It is printed first.
# Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

# Note: The string S has at least 3 distinct characters.


#!/bin/python3

import math
import os
import random
import re
import sys



from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # Count the frequency of each character
    frequency = Counter(s)
    
    # Sort characters by frequency (descending) and then alphabetically
    sorted_characters = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
    # Output the top three characters and their counts
    for i in range(min(3, len(sorted_characters))):
        char, count = sorted_characters[i]
        print(f"{char} {count}")
