price = int(input("투자 금액 : "))
total = price
days = int(input("투자 일수 : "))
rate = list(map(int, input("변동 폭 : ").split()))

for i in rate:
    total *= (1 + rate/100)
    total = int(total)

print(total - price)
