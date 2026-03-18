from collections import deque

def BFS(row, col, cnt, break_cnt):

    global result

    q = deque()
    q.append([row, col, cnt, break_cnt])
    visited[row][col][break_cnt] = True
    while q:
        x, y, tmp, bcnt = q.popleft()
        if tmp > result:
            continue
        if x == N-1 and y == M-1:
            if tmp <= result:
                result = tmp
            return
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 0 and not visited[nx][ny][bcnt]:
                visited[nx][ny][bcnt] = True
                q.append([nx, ny, tmp+1, bcnt])
            elif 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and bcnt == 1 and not visited[nx][ny][bcnt-1]:
                visited[nx][ny][bcnt-1] = True
                q.append([nx, ny, tmp+1, bcnt-1])

N, M = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
result = 0xfffffff

BFS(0, 0, 1, 1)

if result == 0xfffffff:
    print(-1)
else:
    print(result)
