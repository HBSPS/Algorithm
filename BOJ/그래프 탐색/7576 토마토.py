# 7576 토마토

# 모든 영역이 인접해 있는지 그래프를 돌면서 탐색 -> 그래프 탐색
    # 매 반복마다 끝까지 가는 깊이 우선이 아니라 매 반복마다 자신의 인접한 노드로 이동 -> 너비 우선 탐색

# 2차원 배열을 사용
    # 각 노드에서 갈 수 있는 위치를 ds, dy 배열에 저장
        # dx, dy를 사용하여 노드를 이동하는데, 2차원 배열의 범위를 벗어나지 않도록 if문 사용

# 하루가 지나는 것을 2차원 배열에서 경과된 일수로 기록 -> 첫 날 = 1, 둘째날 = 2
    # 단, 시작이 1이므로 결과에서 1을 빼고 출력해야 함

# BFS는 덱을 사용하는데 덱에 요소가 없을때 까지 진행 => 재귀를 돌릴 필요 없음

# 익어있는 토마토가 여러개로 시작하는 경우를 위해 처음에 for문을 사용해 2차원 배열에서 값이 1인 요소의 index를 큐에 넣고 시작

# BFS가 끝나면 각 위치의 토마토가 며칠 뒤 익는지 확인할 수 있음
    # 만약, 0이 있다면 토마토는 다 익을 수 없는 것이므로 -1 출력 => exit(0)을 이용한 프로그램 종료
        # exit을 이용해 종료하지 않게 되면 중복 출력되는 경우 발생

from collections import deque

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dq = deque([]) # 좌표를 넣을 것이기 때문에 배열을 담고있는 deque 선언

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # x와 y 방향으로 움직일 수 있는 경우의 수를 미리 기록 (좌우하상)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            dq.append([i, j]) # 시작할 때, 이미 익어있는 토마토의 위치를 deque에 삽입

def BFS():
    while dq:
        x, y = dq.popleft() # deque에 배열을 넣었기 때문에 좌표를 가져올 수 있음

        for i in range(4):
            a, b = dx[i] + x, dy[i] + y # 이동할 수 있는 경우의 수 (인접한 토마토의 위치)

            if 0 <= a < N and 0 <= b < M and arr[a][b] == 0: # index가 범위를 벗어나지 않으면서 값이 0일 때
                dq.append([a, b]) # deque에 추가하고
                arr[a][b] = arr[x][y] + 1 # 기존의 토마토 값에 1을 더한 값으로 지정 -> 경과된 일 수를 표현하기 위해

BFS()
ans = 0

for i in arr:
    for j in i:
        if j == 0: # 다 익지 않은 경우
            print(-1)
            exit(0) # -1을 출력 후 프로그램 종료

    ans = max(ans, max(i)) # 다 익은 경우, 2차원 배열에서 최댓값을 찾는다

print(ans - 1) # 시작이 1이었기 때문에 -1을 해주고 출력