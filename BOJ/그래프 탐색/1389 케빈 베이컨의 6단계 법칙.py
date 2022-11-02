# 1389 케빈 베이컨의 6단계 법칙

# 케빈 베이컨의 수가 가장 작은 사람을 출력 -> 모든 사람의 케빈 베이컨의 수를 알아야 한다
    # 플로이드 - 워셜을 이용해서 모든 사람들의 최단 경로를 알아야 한다
    # 친구관계는 일방적이지 않기 때문에 무향 그래프로 해결

import math

N, M = map(int, input().split())

arr = [[math.inf for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    arr[a][b] = 1
    arr[b][a] = 1
    arr[a][a] = 0
    arr[b][b] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

minimum = math.inf
answer = 0

for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        tmp += arr[i][j]

    if tmp < minimum:
        minimum = tmp
        answer = i

print(answer)