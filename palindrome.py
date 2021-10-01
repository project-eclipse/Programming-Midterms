[n, count] = [int(input()), 0]
while str(n) != str(n)[::-1]: [n, count] = [n+int(str(n)[::-1]),count+1]
print("%d %d" % (count, n))

