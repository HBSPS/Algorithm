# 2667 단지번호붙이기

# 그래프 탐색
    # BFS를 통해 각 집의 갯수를 배열에 넣는 방법
    # 방문 확인은 그래프의 숫자를 0으로 바꾸는 방법
        # for 중첩을 통해 시작점을 찾고 해당 위치에서 BFS를 돌리며 방문한 곳은 0으로 바꾼다
        # 큐에서 원소를 popleft 할 때 마다 count 증가

from collections import deque

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(a, b):
    dq = deque()
    count = 1
    dq.append([a, b])
    arr[a][b] = 0

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < N and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                dq.append([nx, ny])
                count += 1
    
    return count

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            answer.append(BFS(i, j))

answer.sort()

print(len(answer))

for i in answer:
    print(i)