# 7569 토마토

# 저번에 BFS로 풀었던 토마토 문제와 비슷한 문제 -> 차이점이 있다면 x, y좌표에 z좌표가 추가되었다는 것
    # 같은 방법으로 풀되, 조건이 추가되고 z축으로의 이동을 고려한다면 마찬가지로 BFS로 해결 가능

# z축 구현 방법
    # 기존의 2차원 배열을 새로운 배열에 넣는다
        # 만들어진 새로운 배열에서 첫번째 index가 z축이 된다
            # arr[z][y][x] -> 3차원 배열의 요소에 접근하는 방법

from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

dq = deque()

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

arr = []

for _ in range(H):
    tmp = [list(map(int, input().split())) for _ in range(N)]
    arr.append(tmp)

for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1: # arr[z][y][x]
                dq.append([h, n, m])

def BFS():
    while dq:
        z, y, x = dq.popleft()

        for i in range(6):
            a, b, c = dx[i] + x, dy[i] + y, dz[i] + z

            if 0 <= a < M and 0 <= b < N and 0 <= c < H and arr[c][b][a] == 0:
                dq.append([c, b, a])

                arr[c][b][a] = arr[z][y][x] + 1

BFS()
ans = 0

for h in arr:
    for y in h:
        for x in y:
            if x == 0:
                print(-1)
                exit(0)

            ans = max(ans, max(y))

print(ans-1)