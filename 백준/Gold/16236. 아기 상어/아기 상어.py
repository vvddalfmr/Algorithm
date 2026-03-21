def BFS(v):

    global sec
    global b_shk
    global ocn
    global b_shk_size

    q = []
    visited = [[0] * n for _ in range(n)]

    q.append([v[0], v[1], 0])
    visited[v[0]][v[1]] = 1

    candidates = []

    while q:
        x, y, dist = q.pop(0)

        for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and ocn[nx][ny] <= b_shk_size:
                    visited[nx][ny] = 1

                    if 0 < ocn[nx][ny] < b_shk_size:
                        candidates.append((dist+1, nx, ny))

                    q.append([nx, ny, dist+1])

    if not candidates:
        return False

    candidates.sort()
    dist, fx, fy = candidates[0]

    sec += dist

    b_shk[0], b_shk[1] = fx, fy
    ocn[fx][fy] = 0

    return True

n = int(input())
ocn = [list(map(int, input().split())) for _ in range(n)]
b_shk = [0, 0]
b_shk_size = 2
f_lst = []
f_size_lst = [0, 0, 0, 0, 0, 0]
sec = 0
can_eat = 0

for i in range(n):
    for j in range(n):
        if ocn[i][j] == 9:
            b_shk[0] = i
            b_shk[1] = j
            ocn[i][j] = 0
        elif ocn[i][j] in [1, 2, 3, 4, 5, 6]:
            f_lst.append([i, j, ocn[i][j]])

for k in range(6):
    cnt = 0
    for row in f_lst:
        if row[2] == k+1:
            cnt += 1
    f_size_lst[k] = cnt

can_eat = f_size_lst[0]

eat_count = 0

while True:
    if not BFS(b_shk):
        break

    eat_count += 1

    if eat_count == b_shk_size:
        b_shk_size += 1
        eat_count = 0

print(sec)