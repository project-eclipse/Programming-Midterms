# 2차원 생명게임 구현하기 (컨볼루션 사용 X)

num = int(input("# of iterations: "))
print("Input Board: ")
Board = []
while True:  # 초기 상태의 모습을 입력받아 2차원 배열로 저장하는 부분
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
        for j in range(len(Board)):  # sum이라는 변수에 인접한 세포들 중 몇 개가 살아있는지 저장한다.
            if i == 0:  # 여기서부터는 특수한 케이스 (맵 구석에 위치한 세포)들에 대한 예외 처리
                if j == 0:
                    sum = Board[i][j + 1] + Board[i + 1][j] + Board[i + 1][j + 1]
                elif j == len(Board) - 1:
                    sum = Board[i][j - 1] + Board[i + 1][j - 1] + Board[i + 1][j]
                else:
                    sum = (
                        Board[i][j - 1]
                        + Board[i][j + 1]
                        + Board[i + 1][j - 1]
                        + Board[i + 1][j]
                        + Board[i + 1][j + 1]
                    )
            elif i == len(Board) - 1:
                if j == 0:
                    sum = Board[i - 1][j] + Board[i - 1][j + 1] + Board[i][j + 1]
                elif j == len(Board) - 1:
                    sum = Board[i - 1][j - 1] + Board[i - 1][j] + Board[i][j - 1]
                else:
                    sum = (
                        Board[i - 1][j - 1]
                        + Board[i - 1][j]
                        + Board[i - 1][j + 1]
                        + Board[i][j - 1]
                        + Board[i][j + 1]
                    )
            elif j == 0:
                sum = (
                    Board[i - 1][j]
                    + Board[i - 1][j + 1]
                    + Board[i][j + 1]
                    + Board[i + 1][j]
                    + Board[i + 1][j + 1]
                )
            elif j == len(Board) - 1:
                sum = (
                    Board[i - 1][j - 1]
                    + Board[i - 1][j]
                    + Board[i][j - 1]
                    + Board[i + 1][j - 1]
                    + Board[i + 1][j]
                )
            else:  # 일반적인 경우에는 그냥 주변 8개의 세포들의 값을 더한 것이 sum이 된다.
                sum = (
                    Board[i - 1][j - 1]
                    + Board[i - 1][j]
                    + Board[i - 1][j + 1]
                    + Board[i][j - 1]
                    + Board[i][j + 1]
                    + Board[i + 1][j - 1]
                    + Board[i + 1][j]
                    + Board[i + 1][j + 1]
                )

            if sum == 3:  # 여기서부터는 sum값을 토대로 세포가 다음 세대에 죽었는지 살았는지 판단한다
                NewBoard[i].append(1)
            elif sum == 2 and Board[i][j] == 1:
                NewBoard[i].append(1)
            else:
                NewBoard[i].append(0)
    Board = NewBoard.copy()  # 다음 세대의 값들을 저장한 NewBoard를 현재 세대를 의미하는 Board에 다시 저장한다


def Print(Board):  # 결과를 출력하는 함수
    for i in Board:
        for j in i:
            if j == 0:
                j = "·"
            print(j, end=" ")
        print("")


Print(Board)
print("")
for i in range(num):  # 1세대 ~ n세대까지 출력한다
    iteration()
    Print(Board)
    print("")
