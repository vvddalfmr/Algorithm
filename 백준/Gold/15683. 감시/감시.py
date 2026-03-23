dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dirs = [
    [],
    [[0], [1], [2], [3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3], [3,0]],
    [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    [[0,1,2,3]]
]

def start(x, y, direction, board):

    changed = []

    for d in direction:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx[d], ny + dy[d]
            if not (0 <= nx < N and 0 <= ny < M):
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'
                changed.append((nx, ny))

    return changed

def DFS(cctv_idx, board):

    global result

    if cctv_idx == len(cctv_lst):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt += 1
        result = min(result, cnt)
        return

    x, y, typ = cctv_lst[cctv_idx]

    for direction in dirs[typ]:
        changed = start(x, y, direction, board)
        DFS(cctv_idx + 1, board)
        for cx, cy in changed:
            board[cx][cy] = 0

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cctv_lst = []
result = 0xffffffffffff

for row in range(N):
    for col in range(M):
        if 1 <= room[row][col] <= 5:
            cctv_lst.append((row, col, room[row][col]))

DFS(0, room)

print(result)