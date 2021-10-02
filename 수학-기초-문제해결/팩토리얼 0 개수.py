n = int(input())
two = 0
five = 0
for i in range(n):
    j = i + 1
    while j % 2 == 0:
        two += 1
        j /= 2
    j = i + 1
    while j % 5 == 0:
        five += 1
        j /= 5

print(min(two, five))
