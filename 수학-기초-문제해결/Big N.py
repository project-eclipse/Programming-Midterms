n = int(input())
if not (n%2): raise Exception('입력한 수가 짝수입니다.')
for i in range(n):
    for j in range(n):
        c =(' ', 'N')[(j==0) or (j==n-1) or (i==j)]
        print(c,end=' ')
    print('')