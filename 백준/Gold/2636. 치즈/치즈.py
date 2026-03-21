from collections import deque

def BFS():

    global last_cheese

    visited = [[False] * M for _ in range(N)]
    melted_cheese = 0
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
            elif 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = 0
                melted_cheese += 1
                continue
    last_cheese = melted_cheese

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
hour = 0
last_cheese = 0

while True:

    cheese_cnt = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                cheese_cnt += 1
    if cheese_cnt == 0:
        break
    elif cheese_cnt > 0:
        BFS()
        hour += 1

print(hour)
print(last_cheese)
