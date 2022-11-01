# 11403 경로 찾기

# 인접 행렬
    # 유향 그래프

# 플로이드-워셜 알고리즘

from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()