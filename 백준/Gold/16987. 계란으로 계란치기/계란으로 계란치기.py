def brk_egg(idx):

    global cur_S
    global result
    global broken_lst
    global brk_egg_tot

    if idx == N:
        cnt = 0
        for brk in broken_lst:
            if brk:
                cnt += 1
        result = max(result, cnt)
        return

    if broken_lst[idx]:
        brk_egg(idx+1)
        return

    hit = False
    for i in range(N):
        if i != idx and not broken_lst[i]:
            hit = True

            cur_S[idx] -= egg_box[i][1]
            cur_S[i] -= egg_box[idx][1]

            prev_i = broken_lst[i]
            prev_idx = broken_lst[idx]

            if cur_S[i] <= 0:
                broken_lst[i] = True
            if cur_S[idx] <= 0:
                broken_lst[idx] = True

            brk_egg(idx+1)

            cur_S[idx] += egg_box[i][1]
            cur_S[i] += egg_box[idx][1]
            broken_lst[idx] = prev_idx
            broken_lst[i] = prev_i

    if not hit:
        brk_egg(idx+1)

N = int(input())
egg_box = [list(map(int, input().split())) for _ in range(N)]
cur_S = [0] * N
broken_lst = [False] * N
result = 0
brk_egg_tot = 0

for idx in range(N):
    cur_S[idx] = egg_box[idx][0]

brk_egg(0)

print(result)
