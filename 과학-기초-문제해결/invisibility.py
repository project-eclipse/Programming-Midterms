# 투명 망토 문제 (Bridge and Torch Problem)
# 코드 자체보다는 알고리즘이 중요한 문제라서 따로 주석은 안 달았고, 대신 알고리즘을 설명하는 순서도를 그림
# 알고리즘이 왜 타당한지는 https://link.springer.com/article/10.1007/s43069-020-00022-3 참고 (논문)

entrance = list(map(int,input().split()))
entrance.sort()
time = 0

dormitory = []
a = entrance[0]
try:
    b = entrance[1]
except:
    time = a
    entrance.pop()
tick = 0

while(len(entrance) != 0):
    if not (tick%2):
        if (a in entrance and b in entrance):
            if len(entrance) == 3:
                c = entrance[len(entrance)-1]
                time += c
                dormitory.append(a)
                dormitory.append(c)
                del entrance[0]
                del entrance[-1]
            else:
                time += b
                dormitory.append(entrance[0])
                dormitory.append(entrance[1])
                del entrance[0]
                del entrance[0]
        else:
            c = entrance[len(entrance)-1]
            time += c
            d = entrance[len(entrance)-2]
            dormitory.append(c)
            dormitory.append(d)
            entrance.remove(c)
            entrance.remove(d)
    else:
        if a in dormitory:
            dormitory.remove(a)
            entrance.append(a)
            time += a
        else:
            dormitory.remove(b)
            entrance.append(b)
            time += b
    tick += 1
    entrance.sort()
    dormitory.sort()
    # print(entrance, dormitory, time, tick%2) <- 이 코드를 넣으면 이동 과정을 상세히 볼 수 있다

print(time)

















