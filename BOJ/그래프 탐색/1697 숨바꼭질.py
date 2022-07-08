from collections import deque

dq = deque()
visit = [0] * 100001
tmp = []

N, K = map(int, input().split())

def BFS(N):
    dq.append(N)

    while dq:
        N = dq.popleft()

        if N == K:
            print(visit[K])
            break
        for i in (N + 1, N - 1, N * 2):
            if 0 <= i < 100001 and visit[i] == 0:
                visit[i] = visit[N] + 1
                dq.append(i)

BFS(N)