def sumfact(n):
    sumf = 0
    for i in range(n):
        if i == 0:
            continue
        if not (n % i):
            sumf += i
    return sumf


n = int(input())
sumf = []
for i in range(n):
    sumf.append(sumfact(i + 1))

for i in range(n):
    for j in range(n):
        if (i < j) and (sumf[i] == j + 1) and (sumf[j] == i + 1):
            print("(%d, %d)" % (i + 1, j + 1))

