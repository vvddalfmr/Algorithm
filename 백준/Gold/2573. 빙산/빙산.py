from collections import deque

def BFS_find():

    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for row in range(N):
        for col in range(M):
            if ocn[row][col] > 0 and not visited[row][col]:
                cnt += 1
                q = deque()
                q.append((row, col))
                visited[row][col] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if ocn[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    return cnt

def BFS():

    ice_side_map = [[0] * M for _ in range(N)]
    nb_ice_cnt = 1
    q = deque()
    for row in range(N):
        for col in range(M):
            if ocn[row][col] <= 0:
                q.append((row, col))
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and ocn[nx][ny] == 0:
                continue
            elif 0 <= nx < N and 0 <= ny < M and ocn[nx][ny] > 0:
                ice_side_map[nx][ny] += 1

    for row in range(N):
        for col in range(M):
            if ice_side_map[row][col] > 0:
                ocn[row][col] -= ice_side_map[row][col]

    for i in range(N):
        for j in range(M):
            if ocn[i][j] > 0 :
                nb_ice_cnt += 1

    return nb_ice_cnt

N, M = map(int, input().split())
ocn = [list(map(int, input().split())) for _ in range(N)]
hour = 0

while True:

    ice_cnt = 0
    for row in range(N):
        for col in range(M):
            if ocn[row][col] > 0:
                ice_cnt += 1

    if ice_cnt == 0:
        hour = 0
        break
    else:
        hour += 1
        BFS()
        after_nearby_ice = BFS_find()
        if after_nearby_ice >= 2:
            break

print(hour)