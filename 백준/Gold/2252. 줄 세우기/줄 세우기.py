n, m = list(map(int, input().split()))
st_lst = [list(map(int, input().split())) for _ in range(m)]

def BFS(a):

    global result
    global degree
    global q

    while q:
        t = q.pop(0)
        result.append(t)
        for k in graph[t]:
            if k != 0:
                degree[k] -= 1
                if degree[k] == 0:
                    q.append(k)

graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
result = []
q = []

for i in range(m):
    degree[st_lst[i][1]] += 1
    graph[st_lst[i][0]].append(st_lst[i][1])
for j in range(1, n+1):
    if degree[j] == 0:
        q.append(j)

BFS(0)

print(*result)
