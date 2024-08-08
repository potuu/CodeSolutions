# You are given a complex z. Your task is to convert it to polar coordinates.

# Input Format

# A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

# Constraints

# Given number is a valid complex number

# Output Format
# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of p.

# Sample Input
#   1+2j

# Sample Output
#  2.23606797749979 
#  1.1071487177940904

# Note: The output should be correct up to 3 decimal places.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

number = complex(input())
r = abs(number)
p = cmath.phase(number)
print(r)
print(p)
