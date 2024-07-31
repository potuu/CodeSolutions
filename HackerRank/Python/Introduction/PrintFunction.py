


if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i,end='')

###### Basic Data Types ######

### List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lst = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n]
print(lst)
