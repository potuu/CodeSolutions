# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

# Sample Input
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output
# 5
# 9
# 11
# 12



# Enter your code here. Read input from STDIN. Print output to STDOUT


n1 = int(input())
set_a = set(map(int,input().split()))
n2 = int(input())
set_b = set(map(int,input().split()))
a = (set_a.difference(set_b))
b = (set_b.difference(set_a))
c = a.union(b)
for i in sorted(c):
        print (i)
