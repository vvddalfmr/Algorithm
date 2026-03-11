from itertools import product
from copy import deepcopy

def delta(idx, val):

    global arr
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    used = [[False] * n for _ in range(n)]

    if idx % 2 == 0:
        for row in range(n):
            for col in range(n):
                if c_arr[row][col] != 0:

                    x, y = row, col   # 현재 위치 따로 저장

                    # 먼저 0을 만나면 끝까지 이동
                    while True:
                        nx = x + direction[idx][0]
                        ny = y + direction[idx][1]

                        if not (0 <= nx < n and 0 <= ny < n):
                            break

                        if c_arr[nx][ny] == 0:
                            c_arr[nx][ny] = c_arr[x][y]
                            c_arr[x][y] = 0
                            x, y = nx, ny
                        else:
                            break

                    # 이동 끝난 후 합치기 검사
                    nx = x + direction[idx][0]
                    ny = y + direction[idx][1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if c_arr[nx][ny] == c_arr[x][y] and not used[nx][ny]:
                            c_arr[nx][ny] *= 2
                            c_arr[x][y] = 0
                            used[nx][ny] = True

                            if c_arr[nx][ny] >= val:
                                val = c_arr[nx][ny]

    else:
        for row in range(n-1, -1, -1):
            for col in range(n-1, -1, -1):
                if c_arr[row][col] != 0:

                    x, y = row, col

                    # 먼저 끝까지 이동
                    while True:
                        nx = x + direction[idx][0]
                        ny = y + direction[idx][1]

                        if not (0 <= nx < n and 0 <= ny < n):
                            break

                        if c_arr[nx][ny] == 0:
                            c_arr[nx][ny] = c_arr[x][y]
                            c_arr[x][y] = 0
                            x, y = nx, ny
                        else:
                            break

                    # 이동 후 합치기
                    nx = x + direction[idx][0]
                    ny = y + direction[idx][1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if c_arr[nx][ny] == c_arr[x][y] and not used[nx][ny]:
                            c_arr[nx][ny] *= 2
                            c_arr[x][y] = 0
                            used[nx][ny] = True

                            if c_arr[nx][ny] >= val:
                                val = c_arr[nx][ny]

    return val

def DFS(direct, val, cnt):

    if cnt == 5:
        return val

    if direct[cnt] == 1:
        return DFS(direct, delta(0, val), cnt + 1)
    elif direct[cnt] == 2:
        return DFS(direct, delta(1, val), cnt + 1)
    elif direct[cnt] == 3:
        return DFS(direct, delta(2, val), cnt + 1)
    elif direct[cnt] == 4:
        return DFS(direct, delta(3, val), cnt + 1)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
direct_lst = [1, 2, 3, 4]  # 1은 상 2는 하 3은 좌 4 우 방향으로 진행
result = 0

for col in range(n):
    for row in range(n):
        if arr[row][col] > result:
            result = arr[row][col]

for permt in product(direct_lst, repeat=5): # 중복순열 생성으로 진행방향 고정
    c_arr = deepcopy(arr)
    DFS_result = DFS(list(permt), 0, 0)
    if result <= DFS_result:
        result = DFS_result

print(result)