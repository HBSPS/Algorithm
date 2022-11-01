# 14442 벽 부수고 이동하기 2

# 벽 부수고 이동하기 1과 동일한 과정
    # 단, 이 문제는 부술 수 있는 벽의 개수가 여러개 일 수 있다

from collections import deque

N, M, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input())))

visit = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dq = deque([])
dq.append([0, 0, 0])
visit[0][0][0] = 1

def BFS():
    while dq:
        x, y, h = dq.popleft()

        if x == N-1 and y == M-1:
            return visit[x][y][h]

        for i in range(4):
            a, b = x + dx[i], y + dy[i]

            if a < 0 or a >= N or b < 0 or b >= M:
                continue
            
            if arr[a][b] == 1 and h+1 <= K and visit[a][b][h+1] == 0: # 마지막 조건을 넣어주지 않는다면 시간초과 -> 방문 했던 경우도 큐에 집어넣기 때문에 중복 연산
                visit[a][b][h+1] = visit[x][y][h] + 1
                dq.append([a, b, h+1])
            elif arr[a][b] == 0 and visit[a][b][h] == 0:
                visit[a][b][h] = visit[x][y][h] + 1
                dq.append([a, b, h])

    return -1

print(BFS())