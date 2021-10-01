graph = ['placeholder', [3, 4], [3, 7], [1, 2, 4, 5], [1, 5, 6], [3, 4, 6, 7], [4, 5], [2, 5]] # 인접 리스트로 그래프를 입력받는다.
start = int(input()) # DFS를 시작하게 되는 노드

chk = []

def dfs(start):
    global chk
    now = start
    print(now,end = ' ')
    chk.append(now)
    for next in graph[start]:
        cont = False
        if next in chk:
            continue
        dfs(next)

dfs(start)
print('')