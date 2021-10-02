# 주어진 그래프를 DFS로 탐색하고 결과 출력하기

graph = [
    "placeholder",
    [3, 4],
    [3, 7],
    [1, 2, 4, 5],
    [1, 5, 6],
    [3, 4, 6, 7],
    [4, 5],
    [2, 5],
]  # 그래프를 인접 리스트로 표현함. (리스트의 i번째 요소는 노드 i와 연결된 모든 노드의 리스트임)
start = int(input())  # DFS를 시작하게 되는 노드

chk = []  # chk에 포함된 노드는 이미 탐색되었다는 뜻이다


def dfs(start):  # start에 해당하는 노드를 탐색하자.
    global chk
    print(start, end=" ")  # 먼저 start를 탐색했다는 의미에서 start를 출력하고,
    chk.append(start)  # start를 이미 탐색된 노드들의 리스트에 추가한다.
    for next in graph[start]:
        if next in chk:
            continue
        dfs(next)  # 그리고 start와 인접했는데, 아직 탐색이 안 된 모든 노드에 대해 dfs 함수를 재귀적으로 호출한다.
        # 그러면 인접한 노드를 따라 갈 수 있는 데까지 탐색한 뒤, 더 이상 인접한 노드가 없으면 인접한 노드가 생길 때까지 백트래킹을 하는 DFS가 구현된다.


dfs(start)
print("")
