# 11724 연결 요소의 개수

# 연결 요소의 개수를 구하기 -> 그래프 전체를 탐색해야 하므로 DFS/BFS
    # 연결 요소의 개수를 구하는 것 = 각 그래프 묶음의 개수
        # 따라서, 기존의 DFS/BFS에 for문을 사용해 시작 노드와 연결되지 않은 노드들에 대해서도 탐색을 해야한다

# sys.setrecursionlimit을 설정하여 최대 반복 횟수를 증가시킨다
    # 또한, 입력의 개수가 많으므로 sys.stdin.readline을 사용한다

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

visit = [0 for _ in range(N+1)]

def DFS(start):

    visit[start] = 1
    arr[start].sort()

    for i in arr[start]:
        if visit[i] == 0:
            DFS(i)

for _ in range(M):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

ans = 0

for i in range(1, N+1):
    if visit[i] == 0:
        ans += 1
        DFS(i)

print(ans)