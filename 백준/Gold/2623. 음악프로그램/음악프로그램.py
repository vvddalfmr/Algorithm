def BFS():
    global degree
    global result_arr

    q = []
    for k in range(1, n+1):
        if degree[k] == 0:
            q.append(k)
    while q:
        t = q.pop(0)
        result_arr.append(t)
        for w in graph[t]:
            degree[w] -= 1
            if degree[w] == 0:
                q.append(w)

n, m = list(map(int, input().split()))  # n은 가수의 수 m은 pd의 수
sgr_lst = [list(map(int, input().split())) for _ in range(m)]

result_arr = []
degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    for j in range(1, sgr_lst[i][0]):
        graph[sgr_lst[i][j]].append(sgr_lst[i][j+1])

for row in range(1, n+1):
    for col in range(len(graph[row])):
        degree[graph[row][col]] += 1

BFS()

if len(result_arr) != n:
    print(0)
else:
    for x in result_arr:
        print(x)
