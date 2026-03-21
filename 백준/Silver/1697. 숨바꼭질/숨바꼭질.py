def BFS(n, k, cnt):
    q = []
    q.append([n, 0])
    visited[n] = 1
    while q:
        t = q.pop(0)
        if t[0] == k:
            return t[1]
        for i in [t[0]+1, t[0]-1, t[0]*2]:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = 1
                q.append([i, t[1] + 1])

n, k = list(map(int, input().split()))

visited = [0] * 100001
result = BFS(n, k, 0)

print(result)