# 24479 알고리즘 수업 - 깊이 우선 탐색 1

# DFS 사용
    # 방문 노드를 오름차순 정렬하기 때문에 sort 사용

# point -> global을 사용해 전역변수로 처리해야 한다
    # 전역변수를 사용하지 않으면 중복된 값이 들어갈 수 있다 -> 틀렸습니다 출력

# sys.stdin.readline까지 사용해야 시간초과 X
    # 또한, 기존에 하던 방식처럼 arr[a].append(b)와 arr[b].append(a)를 할 때 마다 sort를 하는 것이 아니라, BFS 재귀 내에서 그때그때 sort하는 것이 시간 복잡도를 줄여준다
        # 만약, 기존처럼 그때그때 sort하는 경우 for문 안에 있기 때문에 for문이 오래 반복될 수록 시간 복잡도가 크게 증가한다

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, R = map(int, input().split())

cnt = 1

visit = [0 for _ in range(N+1)]
arr = [[]for _ in range(N+1)]

def DFS(start):

    global cnt

    visit[start] = cnt
    arr[start].sort()

    for i in arr[start]:
        if visit[i] == 0:
            cnt += 1
            DFS(i)

for i in range(M):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

DFS(R)

for i in range(1, N+1):
    print(visit[i])