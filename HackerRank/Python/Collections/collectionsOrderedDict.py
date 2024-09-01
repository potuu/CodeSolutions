# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# Input Format
# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.

# Constraints
# 0<N<=100

# Output Format
# Print the item_name and net_price in order of its first occurrence.

# Sample Input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# Sample Output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

# Explanation
# BANANA FRIES: Quantity bought: 1, Price: 12
# Net Price: 12
# POTATO CHIPS: Quantity bought: 2, Price: 30
# Net Price: 60
# APPLE JUICE: Quantity bought: 2, Price: 10
# Net Price: 20
# CANDY: Quantity bought: 4, Price: 5
# Net Price: 20

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

# Read number of items
n = int(input().strip())

# Create an ordered dictionary to store net prices
item_dict = OrderedDict()

# Process each item entry
for _ in range(n):
    line = input().strip()
    *item_name_parts, price = line.split()
    item_name = ' '.join(item_name_parts)
    price = int(price)
    
    if item_name in item_dict:
        item_dict[item_name] += price
    else:
        item_dict[item_name] = price

# Print the results
for item, net_price in item_dict.items():
    print(f"{item} {net_price}")

