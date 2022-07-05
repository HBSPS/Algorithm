from collections import deque

N, M, V = map(int, input().split())

l = [[] for _ in range(N+1)]

dq = deque()

start = V

def DFS(start):
    if visit[start] != 1:
        visit[start] = 1

        print(start, end=" ")

        for i in l[start]:
            if visit[i] != 1:
                
                DFS(i)

def BFS(start):
    dq.append(start)
    visit[start] = 1

    while dq:
        start = dq.popleft()

        for i in l[start]:
            if visit[i] != 1:
                dq.append(i)
                visit[i] = 1
        
        print(start, end=" ")


for _ in range(M):
    a, b = map(int, input().split())

    l[a].extend([b])
    l[a].sort()
    l[b].extend([a])
    l[b].sort()

visit = [0 for _ in range(N + 1)]
DFS(V)
print()
visit = [0 for _ in range(N + 1)]
BFS(V)