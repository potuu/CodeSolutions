# You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# Note: Each input line ends with a "\n" character.

# Constraints:
# 1<=n<=10^5
# The sum of the lengths of all the words do not exceed 10^6
# All the words are composed of lowercase English letters only.

# Input Format
# The first line contains the integer, n.
# The next  lines each contain a word.

# Output Format

# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
# 3
# 2 1 1

# Explanation
# There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

# Number of words
n = int(data[0])

# Initialize dictionary for counts and list for order
word_count = defaultdict(int)
order = []

# Process each word
for i in range(1, n + 1):
    word = data[i]
    if word not in word_count:
        order.append(word)
    word_count[word] += 1

# Output number of distinct words
print(len(order))

# Output number of occurrences for each distinct word in order of appearance
print(' '.join(str(word_count[word]) for word in order))
