# 2178 미로 탐색

# 단순히 BFS로만 해결 가능

from collections import deque

N, M = map(int, input().split())

arr = []

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(N):
    arr.append(list(map(int, input())))

dq = deque([])
dq.append([0, 0])

def BFS():
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            a, b = x + dx[i], y + dy[i]

            if 0 <= a and a < N and 0 <= b and b < M and arr[a][b] == 1:
                arr[a][b] = arr[x][y] + 1
                dq.append([a, b])

BFS()

print(arr[N-1][M-1])