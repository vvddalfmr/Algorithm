import heapq

def razer(row, col):

    global result

    turn_cnt_map = [[[-1] * 4 for _ in range(W)] for _ in range(H)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pq = []
    for dir in range(4):
        turn_cnt_map[row][col][dir] = 0
        heapq.heappush(pq, (0, row, col, dir))
    while pq:
        cnt, a, b, dirt = heapq.heappop(pq)
        if turn_cnt_map[a][b][dirt] != -1 and cnt > turn_cnt_map[a][b][dirt]:
            continue
        if (a, b) != (x, y) and board[a][b] == 'C':
            result = cnt
            return
        for idx in range(4):
            nx = a + dx[idx]
            ny = b + dy[idx]
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == '*':
                    continue
                if board[nx][ny] == 'C' or board[nx][ny] == '.':
                    new_cnt = cnt
                    if idx != dirt:
                        new_cnt = cnt + 1
                    if turn_cnt_map[nx][ny][idx] == -1 or new_cnt < turn_cnt_map[nx][ny][idx]:
                        turn_cnt_map[nx][ny][idx] = new_cnt
                        heapq.heappush(pq, (new_cnt, nx, ny, idx))

W, H = list(map(int, input().split()))
board = [list(input()) for _ in range(H)]
x = 0 ; y = 0
result = 0

for row in range(H):
    for col in range(W):
        if board[row][col] == 'C':
            x = row ; y = col
            break

razer(x, y)

print(result)