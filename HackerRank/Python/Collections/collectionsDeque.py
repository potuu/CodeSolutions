# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Constraints
# 0<N<=100

# Output Format
# Print the space separated elements of deque d.

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
import sys
input = sys.stdin.read

# Read all input data
data = input().splitlines()

# Number of operations
n = int(data[0])

# Initialize an empty deque
d = deque()

# Perform each operation
for i in range(1, n + 1):
    operation = data[i].split()
    command = operation[0]
    
    if command == 'append':
        d.append(operation[1])
    elif command == 'appendleft':
        d.appendleft(operation[1])
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()

# Print the final state of the deque
print(' '.join(d))
