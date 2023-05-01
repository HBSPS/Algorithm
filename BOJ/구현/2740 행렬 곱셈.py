# 2740 행렬 곱셈

N, M = map(int, input().split())

A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

B = []

for _ in range(M):
    B.append(list(map(int, input().split())))

answer = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for index in range(M):
            answer[i][j] += (A[i][index] * B[index][j])

for items in answer:
    for item in items:
        print(item, end=' ')
    print()