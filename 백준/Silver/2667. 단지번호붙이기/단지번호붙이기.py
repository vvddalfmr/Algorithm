def BFS(x, y, apt_sum):

    global visited
    global apt_lst

    q = []
    q.append([x, y])
    visited[x][y] = True
    while q:
        tmp = q.pop(0)
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = tmp[0] + dx
            ny = tmp[1] + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                apt_sum += 1
                q.append([nx, ny])

    apt_lst.append(apt_sum)

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
apt = 0
apt_lst = []

for row in range(n):
    for col in range(n):
        if arr[row][col] == 1 and not visited[row][col]:
            BFS(row, col, 1)
            apt += 1

apt_lst.sort()
print(apt)
for i in apt_lst:
    print(i)