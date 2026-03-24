from itertools import combinations
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(comb):

    global result

    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    connected_cnt = 0
    for row in range(5):
        for col in range(5):

            if (row, col, school[row][col]) in comb and not visited[row][col]:
                connected_cnt += 1
                visited[row][col] = True
                q.append((row, col))

                while q:

                    if connected_cnt == 2:
                        return

                    x, y = q.popleft()
                    for idx in range(4):
                        nx, ny = x + dx[idx], y + dy[idx]
                        if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny, school[nx][ny]) in comb and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

    if connected_cnt == 1:
        result += 1
        return

school = [list(input()) for _ in range(5)]
result = 0
sdt_map = []

for row in range(5):
    for col in range(5):
        sdt_map.append((row, col, school[row][col]))

for comb in combinations(sdt_map, 7):
    S_cnt = 0
    for x, y, k in comb:
        if k == 'S':
            S_cnt += 1
    if S_cnt < 4:
        continue
    BFS(comb)

print(result)
