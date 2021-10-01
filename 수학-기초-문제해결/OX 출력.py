#자연수 n을 입력받아, n*n 정사각형 모양으로 O와 X의 대각선 배열 출력하기

n = int(input())
for i in range(n):
    print('O'*(n-i)+'X'*i)
