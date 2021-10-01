graph = [[2,3],[2,6],[0,1,3,4],[0,2,4,5],[2,3,5,6],[3,4],[1,4,5]]

start = int(input()) - 1
chk = []
def bfs(start):
    global chk
    queue = [start]
    chk.append(start)
    print(start+1,end=' ')
    while queue != []:
        now = queue[0]
        queue.pop(0)
        for node in graph[now]:
            if node in chk:
                continue
            chk.append(node)
            print(node+1,end=' ')
            queue.append(node)

bfs(start)