from itertools import combinations

def BFS(v, s_hm):

    q = []
    visited = [0] * (n+1)
    q.append(v[0])
    visited[v[0]] = 1
    cnt = 0

    while q:
        t = q.pop(0)
        s_hm += hm_list[t-1]

        for i in range(1, len(nb_city[t-1])):
            if visited[nb_city[t-1][i]] == 0 and nb_city[t-1][i] in v:
                q.append(nb_city[t-1][i])
                visited[nb_city[t-1][i]] = 1

    for j in range(1, len(visited)):
        if visited[j] == 1 and j in v:
            cnt += 1
    if cnt != len(v):
        s_hm = 0

    return s_hm

n = int(input())
hm_list = list(map(int, input().split()))
nb_city = [list(map(int, input().split())) for _ in range(n)]

m = len(nb_city)

a_city = []
b_city = []
result = -1
min_hm = 10000

for k in range(1, m//2 + 1):
    for comb in combinations(range(1, n+1), k):
        A = list(comb)
        B = [x for x in range(1, n+1) if x not in A]
        if BFS(A, 0) != 0 and BFS(B, 0) != 0:
            if min_hm > abs(BFS(A, 0) - BFS(B, 0)):
                min_hm = abs(BFS(A, 0) - BFS(B, 0))
                result = min_hm

print(result)