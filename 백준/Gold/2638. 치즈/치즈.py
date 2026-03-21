def BFS():

    visited = [[False] * M for _ in range(N)]
    side_cnt_map = [[0] * M for _ in range(N)]
    q = []
    q.append((0, 0))
    while q:
        x, y = q.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
            elif 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                side_cnt_map[nx][ny] += 1

    for row in range(N):
        for col in range(M):
            if side_cnt_map[row][col] >= 2:
                board[row][col] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
hour = 0

while True:

    cheese_cnt = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                cheese_cnt += 1
    if cheese_cnt == 0:
        break
    else:
        BFS()
        hour += 1

print(hour)