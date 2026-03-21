def BFS(v):

    global result
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        tmp = q.pop(0)
        for j in range(len(graph[tmp])):
            if visited[graph[tmp][j]] == 0:
                result += 1
                q.append(graph[tmp][j])
                visited[graph[tmp][j]] = 1

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
result = 0

for i in range(m):
    graph[arr[i][0]].append(arr[i][1])
    graph[arr[i][1]].append(arr[i][0])

BFS(1)
print(result)