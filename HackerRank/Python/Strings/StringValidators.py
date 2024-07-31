# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format
# A single line containing a string S.

# Constraints
# 0<len(S)<1000

# Output Format
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input
# qA2

# Sample Output
# True
# True
# True
# True
# True



if __name__ == '__main__':
    s = input()
    
    # if s.isalnum():
    #     print("True")
    # else:
    #     print("False")
        
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
