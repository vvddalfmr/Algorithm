def chk(row):

    global board
    global result

    if row == n:
        result += 1
        return

    for col in range(n):
        Queen = False

        if used[col]:
            continue

        x = row - 1 ; y = col - 1
        while not Queen and x >= 0 and y >= 0:
            if board[x][y] == 1:
                Queen = True
                break
            x -= 1 ; y -= 1
        x = row -1 ; y = col + 1
        while not Queen and x >= 0 and y < n:
            if board[x][y] == 1:
                Queen = True
                break
            x -= 1 ; y += 1
        if  not Queen:
            board[row][col] = 1
            used[col] = True
            chk(row + 1)
            board[row][col] = 0
            used[col] = False

n = int(input())
result = 0
board = [[0] * n for _ in range(n)]
used = [False] * n

chk(0)

print(result)