import sys
import heapq
input = sys.stdin.readline
def route(now, val):

    global result_lst
    pq = []
    for idx in range(len(graph[now])):
        heapq.heappush(pq, [val + graph[now][idx][1], graph[now][idx][0]])
    while pq:
        tmp = heapq.heappop(pq)
        sum_val = tmp[0]
        if sum_val > result_lst[tmp[1]]:
            continue
        if sum_val < result_lst[tmp[1]]:
            result_lst[tmp[1]] = tmp[0]
        for idx in range(len(graph[tmp[1]])):
            if sum_val + graph[tmp[1]][idx][1] < result_lst[graph[tmp[1]][idx][0]]:
                result_lst[graph[tmp[1]][idx][0]] = sum_val + graph[tmp[1]][idx][1]
                heapq.heappush(pq, [sum_val + graph[tmp[1]][idx][1], graph[tmp[1]][idx][0]])

V, E = list(map(int, input().split()))    # 정점의 개수 V , 간선의 개수 E
K = int(input())    # 시작 정점의 번호
arr = [list(map(int, input().split())) for _ in range(E)]  # arr의 요소 u, v, w는 u에서 v 정점으로 가는 가중치 w를 나타낸다
graph = [[] for _ in range(V+1)]
result_lst = [0xfffffffffffff] * (V+1)

result_lst[K] = 0
for idx in range(E):
    graph[arr[idx][0]].append([arr[idx][1], arr[idx][2]])

route(K, 0)

for idx in range(1,V+1):
    if result_lst[idx] == 0xfffffffffffff:
        print('INF')
    else:
        print(result_lst[idx])