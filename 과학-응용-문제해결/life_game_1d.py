#1차원 생명게임 구현하기

data = input().split(',') # 초기 상태 및 구하고자 하는 세대가 몇 번쨰인지를 '0110011', 1 과 같이 입력받는다
data[0] = data[0][1:-1] # 문자열 '0110011' 에서 양쪽에 있는 '를 제거한다
data[1] = int(data[1].strip())

def iteration(data): # 1세대 후의 배치 구하기
    result = ''
    for i in range(len(data)):
        result += str(int(data[i])^((int(data[i-1])^int(data[(i+1)%len(data)])))) # 다음 세대의 i번째 칸은 이전 세대의 (i-1)번째 세대와 (i+1)번쨰 세대의 XOR 값이다.
    return result

for i in range(data[1]):
    data[0] = iteration(data[0]) # 원하는 세대를 얻을 때까지 반복
print(data[0])
