# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# Input Format

# Read , the year to test.

# Constraints
#1900<=year<=100000

# Output Format
# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

# Sample Input 0
# 1990

# Sample Output 0
# False

# Explanation 0
# 1990 is not a multiple of 4 hence it's not a leap year.


def is_leap(year):
    leap = False
    
    # Write your logic here
    1900<=year<=10000
    
    # if year==0:
    #     leap = False
    # else:  
    #     if year%4==0:
    #         leap = True  
    # code in comments also works but it doesn't consider information: "1990 is not a multiple of 4 hence it's not a leap year." that's why solution 1 turns False.
    
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap=True
        
    return leap

year = int(input())
print(is_leap(year))
