from itertools import combinations

N, M = list(map(int, input().split()))
city = [list(map(int, input().split())) for _ in range(N)]
chk = []
home = []
result = 100000

for row in range(N):
    for col in range(N):
        if city[row][col] == 1:
            home.append([row, col])
        if city[row][col] == 2:
            chk.append([row, col])

for comb in combinations(chk, M):
    city_dist = 0

    for j in range(len(home)):
        min_chk_dist = 10000

        for i in range(M):
            chk_dist = abs(comb[i][0]-home[j][0]) + abs(comb[i][1]-home[j][1])

            if chk_dist < min_chk_dist:
                min_chk_dist = chk_dist

        city_dist += min_chk_dist

    if city_dist < result:
        result = city_dist

print(result)