from datetime import datetime, date
today = list(map(int,date.today().strftime("%Y,%m,%d").split(",")))
birthday = list(map(int,input("1234/05/01과 같은 방식으로 대상의 생일을 입력하세요. 기원전은 연도 앞에 '-'를 붙입니다. : ").split("/")))

def days(day):
    if (day[1] > 12 or day[1] < 1): raise Exception('달력에 없는 날짜입니다.')
    if (day[0] < 0): day[0] += 1
    if (day[0] == 0): raise Exception('달력에 없는 날짜입니다.')
    day[0] -= 1
    ret = day[0]*365 + day[0]//4 - day[0]//100 + day[0]//400 + day[2] - 1
    lookup = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (not(day[0] % 4) and ((day[0] % 100) or not(day[0] % 400)) and day[1] > 2): lookup[1] += 1
    if (day[2] < 0 or day[2] > lookup[day[1] - 1]): raise Exception('달력에 없는 날짜입니다.')
    for i in range(day[1]):
        ret += lookup[i]
    return ret

print(days(today) - days(birthday))
    



