# 10026 적록색약

# BFS로 해결
    # 적록색약의 경우 R과 G를 구분하지 못한다
    # 배열을 복사하여 새로운 배열을 만든뒤 G를 R로 바꾸고 똑같이 BFS

from collections import deque
import copy

N = int(input())

arr = [list(input()) for _ in range(N)]
arr2 = copy.deepcopy(arr)

for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
answer2 = []

def BFS(a, b, base, arr):
    dq = deque()
    count = 1
    dq.append([a, b])
    arr[a][b] = 0

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < N and arr[nx][ny] == base:
                arr[nx][ny] = 0
                dq.append([nx, ny])
                count += 1
    
    return count

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            answer.append(arr[i][j])
            BFS(i, j, arr[i][j], arr)

        if arr2[i][j] != 0:
            answer2.append(arr2[i][j])
            BFS(i, j, arr2[i][j], arr2)

print(len(answer), len(answer2))