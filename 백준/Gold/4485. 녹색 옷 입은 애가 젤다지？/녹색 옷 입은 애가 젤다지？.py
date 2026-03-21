import heapq

def Darick(xy, val):

    global result

    pq = []
    dist[xy[0]][xy[1]] = val
    heapq.heappush(pq, [val, xy])
    while pq:
        tmp = heapq.heappop(pq)
        new_val = tmp[0]
        if tmp[1][0] != n-1 and tmp[1][1] != n-1 and new_val >= result:
            continue
        if tmp[1][0] == n-1 and tmp[1][1] == n-1 and new_val < result:
            result = new_val
            return
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = tmp[1][0] + dx
            ny = tmp[1][1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = new_val
                    heapq.heappush(pq, [new_val + arr[nx][ny], [nx, ny]])
                elif dist[nx][ny] != -1 and new_val < dist[nx][ny]:
                    dist[nx][ny] = new_val
                    heapq.heappush(pq, [new_val + arr[nx][ny], [nx, ny]])

tc = 0

while True:
    n = int(input())
    if n == 0:
        break
    tc += 1
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[-1] * n for _ in range(n)]
    result = 0xffffffffffffffffff

    Darick([0, 0], arr[0][0])

    print(f'Problem {tc}: {result}')


