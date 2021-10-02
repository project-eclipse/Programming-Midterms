# BFS로 주어진 그래프 탐색하고 결과 출력하기

graph = [
    [2, 3],
    [2, 6],
    [0, 1, 3, 4],
    [0, 2, 4, 5],
    [2, 3, 5, 6],
    [3, 4],
    [1, 4, 5],
]  # 그래프를 인접 리스트로 표현함. (리스트의 i번째 요소는 노드 i와 연결된 모든 노드의 리스트임)
start = int(input()) - 1  # 탐색을 시작할 노드의 위치


def bfs(start):
    chk = []  # chk에 포함된 노드는 이미 발견되었다는 뜻이다
    queue = [
        start
    ]  # 앞으로 탐사하고자 하는 노드를 순서대로 담는 큐. 파이썬에서는 따로 모듈을 사용하지 않고도 리스트만으로 큐를 구현할 수 있다
    chk.append(start)
    print(start + 1, end=" ")  # 첫 번째 노드를 탐색하고, 결과 출력
    while queue != []:  # queue가 비어 있다면, 더 이상 탐색할 노드가 없다는 의미이므로 탐색을 중단해도 된다
        now = queue[0]
        queue.pop(0)  # 탐색할 노드를 의미하는 변수 now에 queue의 첫 번째 요소를 저장한 후, queue에서 그 요소를 삭제한다
        for node in graph[now]:
            if node in chk:
                continue
            chk.append(node)
            print(node + 1, end=" ")
            queue.append(
                node
            )  # now에 해당하는 노드를 탐색한다. now와 인접했고, 아직 발견이 안 된 새로운 노드를 전부 큐에 넣어놓는다.


bfs(start)
