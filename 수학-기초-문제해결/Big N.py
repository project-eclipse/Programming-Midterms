# 커다란 'N' 모양으로 글자 출력하기

n = int(input())
if not (n % 2):
    raise Exception("입력한 수가 짝수입니다.")
for i in range(n):
    for j in range(n):
        c = (" ", "N")[
            (j == 0) or (j == n - 1) or (i == j)
        ]  # "변수 c는 j==0 또는 j==n-1 또는 i==j일 때 'N'으로, 그렇지 않을 때는 ' '으로 설정한다."
        print(c, end=" ")
    print("")
