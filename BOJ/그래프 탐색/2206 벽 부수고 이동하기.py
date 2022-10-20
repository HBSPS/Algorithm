# 2206 벽 부수고 이동하기

# BFS 사용
    # 단, 벽을 한 개 까지 부술 수 있기 때문에 벽을 부수고 난 뒤 인지 확인하는 과정이 필요하다
    # 지도를 두 개 사용한다고 생각하면 됨
        # 만약, 첫번째 지도에 있다면 아직 벽을 부수지 않은 것이고 두번째 지도에 있다면 더이상 벽을 부수지 못한다는 뜻

from collections import deque

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input())))

visit = [[[0]*2 for _ in range(M)] for _ in range(N)]

dq = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dq.append([0, 0, 0]) # x, y, 위, 거리
visit[0][0][0] = 1

def BFS():
    while dq:
        x, y, h = dq.popleft()

        if x == N-1 and y == M-1:
            return visit[x][y][h]

        for i in range(4):
            a, b = dx[i] + x, dy[i] + y

            if a >= N or a < 0 or b >= M or b < 0:
                continue
            if arr[a][b] == 1 and h == 0:
                visit[a][b][1] = visit[x][y][0] + 1
                dq.append([a, b, 1])
            elif arr[a][b] == 0 and visit[a][b][h] == 0:
                visit[a][b][h] = visit[x][y][h] + 1
                dq.append([a, b, h])
        
    return -1

print(BFS())