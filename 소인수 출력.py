n = int(input())
for i in range(n):
    if (i==0 or i==1 or n%i != 0): continue
    while (n%i) == 0:
        n /= i
    print(i, end=' ')