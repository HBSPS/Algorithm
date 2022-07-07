from collections import deque

T = int(input())

ax = [1, -1, 0, 0]
ay = [0, 0, 1, -1]

def BFS(grid, a, b):
    dq = deque()
    dq.append((a,b))
    grid[a][b] = 0

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            new_x = x + ax[i]
            new_y = y + ay[i]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if grid[new_x][new_y] == 1:
                grid[new_x][new_y] = 0
                dq.append((new_x, new_y))
    return

for i in range(T):
    cnt = 0

    N, M, K = map(int, input().split())
    grid = [[0]*M for _ in range(N)]

    for k in range(K):
        x, y = map(int, input().split())
        grid[x][y] = 1

    for a in range(N):
        for b in range(M):
            if grid[a][b] == 1:
                BFS(grid, a, b)
                cnt += 1
    
    print(cnt)