#컨볼루션을 쓰지 않고, 리스트에 패딩도 안 한 자의 비참한 최후

num = int(input('# of iterations: '))
print('Input Board: ')
Board = []
while True:
    line = input()
    if len(line) > 0:
        temp = []
        for i in line:
            temp.append(int(i))
        Board.append(temp)
    else:
        break

def iteration():
    global Board
    NewBoard = []
    for i in range(len(Board)):
        NewBoard.append([])
        for j in range(len(Board)):
            if i==0: # 예외처리로 몸 비틀기
                if j==0: 
                    sum = Board[i][j+1] + Board[i+1][j] + Board[i+1][j+1]
                elif j==len(Board)-1:
                    sum = Board[i][j-1] + Board[i+1][j-1] + Board[i+1][j]
                else:
                    sum = Board[i][j-1] + Board[i][j+1] + Board[i+1][j-1] + Board[i+1][j] + Board[i+1][j+1]
            elif i==len(Board)-1:
                if j==0:
                    sum = Board[i-1][j] + Board[i-1][j+1] + Board[i][j+1]
                elif j==len(Board)-1:
                    sum = Board[i-1][j-1] + Board[i-1][j] + Board[i][j-1]
                else:
                    sum = Board[i-1][j-1] + Board[i-1][j] + Board[i-1][j+1] + Board[i][j-1] + Board[i][j+1]
            elif j==0:
                sum = Board[i-1][j] + Board[i-1][j+1] + Board[i][j+1] + Board[i+1][j] + Board[i+1][j+1]
            elif j==len(Board)-1:
                sum = Board[i-1][j-1] + Board[i-1][j] + Board[i][j-1] + Board[i+1][j-1] + Board[i+1][j]
            else:
                sum = Board[i-1][j-1] + Board[i-1][j] + Board[i-1][j+1] + Board[i][j-1] + Board[i][j+1] + Board[i+1][j-1] + Board[i+1][j] + Board[i+1][j+1]

            if sum == 3:
                NewBoard[i].append(1)
            elif sum == 2 and Board[i][j] == 1:
                NewBoard[i].append(1)
            else:
                NewBoard[i].append(0)
    Board = NewBoard.copy()

def Print(Board):
    for i in Board: 
        for j in i:
            if (j==0): j='·'
            print(j,end=' ')
        print('')
Print(Board)
print('')
for i in range(num):
    iteration()
    Print(Board)
    print('')