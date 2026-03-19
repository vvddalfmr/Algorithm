import sys
input = sys.stdin.readline
import heapq

def fox():

    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        dist_sum, wood_num = heapq.heappop(pq)

        if dist_sum > fox_dist[wood_num]:
            continue

        for nxt_wood, cost in graph[wood_num]:
            if dist_sum + cost < fox_dist[nxt_wood]:
                fox_dist[nxt_wood] = dist_sum + cost
                heapq.heappush(pq, (dist_sum + cost, nxt_wood))
    return

def wolf():

    pq = []
    heapq.heappush(pq, (0, 1, 1))
    while pq:
        dist_sum, wood_num, status = heapq.heappop(pq)

        if status == 1 and dist_sum > wolf_fast[wood_num]:
            continue
        elif status == 2 and dist_sum > wolf_slow[wood_num]:
            continue
        for nxt_wood, cost in graph[wood_num]:
            if status == 1:
                new_dist_sum = dist_sum + cost // 2
                if wolf_slow[nxt_wood] > new_dist_sum:
                    wolf_slow[nxt_wood] = new_dist_sum
                    heapq.heappush(pq, (new_dist_sum, nxt_wood, 2))
            elif status == 2:
                new_dist_sum = dist_sum + cost * 2
                if wolf_fast[nxt_wood] > new_dist_sum:
                    wolf_fast[nxt_wood] = new_dist_sum
                    heapq.heappush(pq, (new_dist_sum, nxt_wood, 1))
    return

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
fox_dist = [0xffffffffffff] * (N+1)
wolf_fast = [0xffffffffffff] * (N+1)
wolf_slow = [0xffffffffffff] * (N+1)
fox_dist[1] = 0
wolf_fast[1] = 0
result = 0

for idx in range(M):
    graph[arr[idx][0]].append([arr[idx][1], arr[idx][2]*2])
    graph[arr[idx][1]].append([arr[idx][0], arr[idx][2]*2])

fox()
wolf()

for moon in range(2, N+1):
    if fox_dist[moon] < wolf_fast[moon] and fox_dist[moon] < wolf_slow[moon]:
        result += 1

print(result)
