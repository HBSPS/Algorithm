# 14940 쉬운 최단거리

from collections import deque

N, M = map(int, input().split())

table = []
dq = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
answer = [[-1 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    tmp = list(map(int, input().split()))

    for j in range(M):
        if tmp[j] == 2:
            dq.append([i, j])
            visited[i][j] = True
            answer[i][j] = 0

        if tmp[j] == 0:
            answer[i][j] = 0
    
    table.append(tmp)

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and table[nx][ny] == 1:
            dq.append([nx, ny])
            visited[nx][ny] = True
            answer[nx][ny] = answer[x][y] + 1

for row in answer:
    for item in row:
        print(item, end=' ')
    print()