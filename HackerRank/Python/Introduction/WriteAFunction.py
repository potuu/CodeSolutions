



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
