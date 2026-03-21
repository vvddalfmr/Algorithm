R, C, T = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]
dust_sum = 0
location = 0

def spread():

    temp = [[0]*C for _ in range(R)]
    temp[location][0] = -1
    temp[location2][0] = -1

    for x in range(R):
        for y in range(C):
            if arr[x][y] > 0:
                spread_amount = arr[x][y] // 5
                cnt = 0
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nx = dx + x
                    ny = dy + y
                    if 0 <= nx < R and 0 <= ny < C:
                        if arr[nx][ny] != -1:
                            temp[nx][ny] += spread_amount
                            cnt += 1
                temp[x][y] += arr[x][y] - (spread_amount * cnt)

    return temp

def wind_up():

    for row in range(location-2, -1, -1):
        arr[row+1][0] = arr[row][0]
    arr[0][0] = 0

    for col in range(1, C):
        arr[0][col-1] = arr[0][col]
    arr[0][C-1] = 0

    for row in range(1, location+1):
        arr[row-1][C-1] = arr[row][C-1]
    arr[location][C-1] = 0

    for col in range(C-2, 0, -1):
        arr[location][col+1] = arr[location][col]
    arr[location][1] = 0

def wind_down():

    for row in range(location2+1, R-1):
        arr[row][0] = arr[row+1][0]
    arr[R-1][0] = 0

    for col in range(1, C):
        arr[R-1][col - 1] = arr[R-1][col]
    arr[R-1][C-1] = 0

    for row in range(R-2, location2-1, -1):
        arr[row+1][C-1] = arr[row][C - 1]
    arr[location2][C-1] = 0

    for col in range(C-2, 0, -1):
        arr[location2][col + 1] = arr[location2][col]
    arr[location2][1] = 0

for row in range(R):
    if arr[row][0] == -1:
        location = row
        break

location2 = location + 1

for sec in range(T):
    arr = spread()
    wind_up()
    wind_down()

for row in range(R):
    for col in range(C):
        if arr[row][col] > 0:
            dust_sum += arr[row][col]

print(dust_sum)