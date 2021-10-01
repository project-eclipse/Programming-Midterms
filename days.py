from datetime import datetime, date
today = list(map(int,date.today().strftime("%Y,%m,%d").split(",")))
birthday = list(map(int,input("1234/05/01과 같은 방식으로 대상의 생일을 입력하세요. : ").split("/")))

def days(day):
    day[0] -= 1
    ret = day[0]*365 + day[0]//4 - day[0]//100 + day[0]//400 + day[2] - 1
    lookup = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (not(day[0] % 4) and ((day[0] % 100) or not(day[0] % 400)) and day[1] > 2): lookup[1] += 1
    for i in range(day[1]):
        ret += lookup[i]
    return ret

print (days(today) - days(birthday))
