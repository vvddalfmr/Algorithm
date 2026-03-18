from collections import deque

def BFS():
    global cnt

    visited = [[False] * N for _ in range(N)]
    moved = False

    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                q = deque()
                q.append((row, col))
                visited[row][col] = True

                population = world[row][col]
                union = [(row, col)]

                while q:
                    x, y = q.popleft()
                    for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            gap = abs(world[x][y] - world[nx][ny])
                            if L <= gap <= R:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                union.append((nx, ny))
                                population += world[nx][ny]

                if len(union) > 1:
                    moved = True
                    new_val = population // len(union)
                    for x, y in union:
                        world[x][y] = new_val

    if moved:
        cnt += 1
    return moved


N, L, R = list(map(int, input().split()))
world = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    if not BFS():
        break

print(cnt)