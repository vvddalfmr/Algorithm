def BFS(a, b):

    visited = [0] * (n+1)
    q = []
    q.append(a)
    visited[a] = 1
    while q:
        tmp = q.pop(0)
        for l in range(len(graph[tmp])):
            if visited[graph[tmp][l]] == 0:
                b += 1
                q.append(graph[tmp][l])
                visited[graph[tmp][l]] = 1
    return b

def BFS_inverse(a, b):

    visited = [0] * (n+1)
    q = []
    q.append(a)
    visited[a] = 1
    while q:
        tmp = q.pop(0)
        for l in range(len(graph_inverse[tmp])):
            if visited[graph_inverse[tmp][l]] == 0:
                b += 1
                q.append(graph_inverse[tmp][l])
                visited[graph_inverse[tmp][l]] = 1
    return b

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] * (n+1) for _ in range(n+1)]
graph_inverse = [[] * (n+1) for _ in range(n+1)]
result = 0

for k in range(m):
    graph[arr[k][0]].append(arr[k][1])
    graph_inverse[arr[k][1]].append(arr[k][0])
for i in range(1, n+1):
    if BFS(i, 0) + BFS_inverse(i, 0) == n-1:
        result += 1

print(result)

