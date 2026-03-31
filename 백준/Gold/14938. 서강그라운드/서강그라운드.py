import heapq

def chk(idx):

    global result

    pq = []
    val_map = [1] * (n+1)
    dist_map = [-1] * (n+1)
    val_map[idx] = -1 * item_lst[idx]
    heapq.heappush(pq, (0, idx))
    while pq:
        dist, x = heapq.heappop(pq)
        for k in range(len(graph[x])):
            new_dist = graph[x][k][1] + dist
            if new_dist <= m and  (dist_map[graph[x][k][0]] == -1 or dist_map[graph[x][k][0]] > new_dist):
                val_map[graph[x][k][0]] = -1 * item_lst[graph[x][k][0]]
                heapq.heappush(pq, (new_dist, graph[x][k][0]))

    tot_val = 0
    for i in range(1, n+1):
        if val_map[i] != 1:
            tot_val += val_map[i]

    result = min(result, tot_val)

n, m, r = map(int, input().split())
item_lst = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
result = 0xffffff

for idx in range(1, n+1):
    chk(idx)

print(-1 * result)