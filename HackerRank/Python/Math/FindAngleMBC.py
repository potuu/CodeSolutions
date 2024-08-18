# ABC is a right triangle, 90 at B.
# Therefore, ABC=90.

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AC and BC.
# Your task is to find MBC(angle theta, as shown in the figure) in degrees.

# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints
# 0<AB<=100
# 0<BC<=100
# Lengths  and  are natural numbers.

# Output Format
# Output MBC in degrees.
# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


# Sample Input
# 10
# 10

# Sample Output
# 45°

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input()) 
BC = int(input())

AC = math.sqrt(AB**2 + BC**2)

print(str(int(round(math.degrees(math.acos(BC/AC))))) + '\u00b0')
