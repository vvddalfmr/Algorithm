from itertools import combinations

def chk(comb):

    for idx in range(1, N+1):
        hgt = 0
        s_point = idx-1
        cur_point = idx-1
        while hgt < H:
            if cur_point < N-1 and bridge[hgt*(N-1) + cur_point] == 0:
                cur_point += 1
            elif cur_point > 0 and bridge[hgt*(N-1) + (cur_point-1)] == 0:
                cur_point -= 1
            hgt += 1

        if s_point != cur_point:
             return False

    return True


N, M, H = map(int, input().split())
ldr = [list(map(int, input().split())) for _ in range(M)]
result = -1
bridge = [1] * ((N-1)*H)
candidates = []

for idx in range(M):
    x = ldr[idx][0]
    y = ldr[idx][1]
    bridge[(x-1)*(N-1) + (y-1)] = 0

for i in range((N-1)*H):
    if bridge[i] == 1:
        candidates.append(i)

for k in range(4):
    for comb in combinations(candidates, k):
        nb_cnt = 0
        for idx in range(k):
            if idx < k-1 and (comb[idx]//(N-1) == comb[idx+1]//(N-1)) and (comb[idx] + 1 == comb[idx+1]):
                nb_cnt += 1
        if nb_cnt == 0:
            for c in comb:
                bridge[c] = 0

            if chk(comb):
                result = k
                print(result)
                exit()

            for c in comb:
                bridge[c] = 1

print(result)