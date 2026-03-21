N, M = map(int, input().split())
arr = list(map(int, input().split()))
pick = []
for k in range(1, N + 1):
    pick.append(k)
result = 0

def find(num):

    global result
    global pick

    idx = 0
    tmp = []
    for k in range(len(pick)):
        if pick[k] == num:
            idx = k
            break

    if idx <= len(pick) // 2:
        result += idx
        tmp += pick[:idx]
        pick = pick[idx:]
        pick = pick + tmp
        pick.pop(0)

    elif idx > len(pick) // 2:
        result += len(pick) - idx
        tmp += pick[idx:]
        pick = pick[:idx]
        pick = tmp + pick
        pick.pop(0)

for idx in range(M):
    find(arr[idx])

print(result)