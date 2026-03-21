def DFS(v):

    global visited

    if visited[v] == 1:
        return
    else:
        visited[v] = 1
        print(v, end = ' ')
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == 0:
                DFS(graph[v][i])

def BFS(v):

    visited_1 = [0] * (n+1)
    q = []
    q.append(v)
    visited_1[v] = 1
    while q:
        t = q.pop(0)
        print(t, end = ' ')
        for i in range(len(graph[t])):
            if visited_1[graph[t][i]] == 0:
                q.append(graph[t][i])
                visited_1[graph[t][i]] = 1

n, m, v = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for row in range(m):
    graph[arr[row][0]].append(arr[row][1])
    graph[arr[row][1]].append(arr[row][0])
for i in range(1, n+1):
    graph[i].sort()

DFS(v)
print()
BFS(v)