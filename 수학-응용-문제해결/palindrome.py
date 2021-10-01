# 회문 수 알고리즘으로 회문수를 만들고, 시행 횟수를 출력하기

[n, count] = [int(input()), 0]
while str(n) != str(n)[::-1]: [n, count] = [n+int(str(n)[::-1]),count+1] # [::-1]은 거꾸로 뒤집은 문자열임을 의미한다.
print("%d %d" % (count, n))

