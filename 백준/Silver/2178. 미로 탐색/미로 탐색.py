def BFS(row, col, dist):

    global result
    visited = [[0] * m for _ in range(n)]
    q = []
    q.append([row, col, dist])
    visited[row][col] = 1
    while q:
        tmp = q.pop(0)
        if tmp[0] == n - 1 and tmp[1] == m - 1:
            result = tmp[2]
            return
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = tmp[0] + dx
            ny = tmp[1] + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny, tmp[2] + 1])
                visited[nx][ny] = 1

n, m = list(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(n)]
result = 0

BFS(0, 0, 1)
print(result)