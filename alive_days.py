from datetime import datetime, date
today = list(map(int,date.today().strftime("%Y,%m,%d").split(",")))
birthday = list(map(int,input("1234/05/01과 같은 방식으로 대상의 생일을 입력하세요. 기원전은 연도 앞에 '-'를 붙입니다. : ").split("/")))

def days(day):
    if (day[1] > 12 or day[1] < 1): raise Exception('달력에 없는 날짜입니다.')
    if (day[0] < 0): day[0] += 1
    if (day[0] == 0): raise Exception('달력에 없는 날짜입니다.')
    if (day[0] == 1581 and day[1] == 10 and (5 <= day[2] and 14 <= day[2])): raise Exception('달력에 없는 날짜입니다.')
    day[0] -= 1
    ret = day[0]*365 + day[0]//4 - day[0]//100 + day[0]//400 + day[2] - 1
    lookup = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (not(day[0] % 4) and ((day[0] % 100) or not(day[0] % 400)) and day[1] > 2): lookup[1] += 1
    if (day[2] < 0 or day[2] > lookup[day[1] - 1]): raise Exception('달력에 없는 날짜입니다.')
    for i in range(day[1]):
        ret += lookup[i]
    if ((day[0] > 1581) or (day[0] == 1581 and day[1] > 10) or (day[0] == 1581 and day[1] == 10 and day[2] > 14)):
        ret -= 10
    else: print("주의: 해당 인물은 현재 사용되는 역법이 도입되기 전에 탄생하였습니다. 만약 인물의 생일을 그레고리력으로 입력하지 않았다면 부정확한 결과가 출력될 수 있습니다.")
    return ret

print(days(today) - days(birthday))
    



