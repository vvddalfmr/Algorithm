import heapq

def hq(val, xy):

    pq = []
    heapq.heappush(pq, [val, xy])
    while pq:
        tmp = heapq.heappop(pq)
        cost = tmp[0]
        if tmp[1][0] == n-1 and tmp[1][1] == n-1:
            return tmp[0]

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = tmp[1][0] + dx
            ny = tmp[1][1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    new_cost = cost + 1
                else:
                    new_cost = cost
                if dist[nx][ny] == -1 or dist[nx][ny] > new_cost:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, [new_cost, [nx, ny]])
                else:
                    if dist[nx][ny] == -1 or dist[nx][ny] > new_cost:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, [new_cost, [nx, ny]])


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

print(hq(0, [0, 0]))
