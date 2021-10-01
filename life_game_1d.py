data = input().split(',')
data[0] = data[0][1:-1]
data[1] = int(data[1].strip())

def iteration(data):
    result = ''
    for i in range(len(data)):
        result += str(int(data[i])^((int(data[i-1])^int(data[(i+1)%len(data)]))))
    return result

for i in range(data[1]):
    data[0] = iteration(data[0])
print(data[0])
