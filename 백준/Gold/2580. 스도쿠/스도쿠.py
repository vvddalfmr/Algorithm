def chk(x, y):

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    used = [False] * 10

    for idx in range(9):
        if board[x][idx] in num:
            used[board[x][idx]] = True
        if board[idx][y] in num:
            used[board[idx][y]] = True

    for row in range(3):
        for col in range(3):
            nx = row + (x//3) * 3
            ny = col + (y//3) * 3
            if board[nx][ny] in num:
                used[board[nx][ny]] = True

    candidate = []
    for use in range(1, 10):
        if not used[use]:
            candidate.append(use)

    return candidate

def DFS(idx):

    if idx == zero_cnt:
        for idx in range(9):
            print(*board[idx])
        exit()

    x, y = zero_lst[idx]
    cand = chk(x, y)
    if not cand:
        return

    n = len(cand)
    i = 0
    while i < n:

        board[x][y] = cand[i]
        DFS(idx + 1)
        board[x][y] = 0
        i += 1

board = [list(map(int, input().split())) for _ in range(9)]
zero_cnt = 0
zero_lst = []

for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            zero_cnt += 1
            zero_lst.append([row, col])

DFS(0)
