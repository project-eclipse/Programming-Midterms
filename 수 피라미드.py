n = int(input())
n -= 1
for i in range(n):
    for j in range(2*n-1):
        c = (i+1)-abs(n-1-j)
        if (c<=0): c = ' '
        print(str(c),end='')
    print('')