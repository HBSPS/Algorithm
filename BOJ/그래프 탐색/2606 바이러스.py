# 2606 바이러스

# DFS와 BFS를 사용해 그래프 탐색을 해야 한다 -> 그래프 전체를 돌며 연결되어 있는 노드들을 찾아야 하므로

def DFS(start):
    if visit[start] != 1:
        visit[start] = 1

        for i in arr[start]:
            if visit[i] != 1:
                DFS(i)

N = int(input())

arr = [[] for _ in range(N+1)]

visit = [0 for _ in range(N+1)]

M = int(input())

for i in range(M):
    a, b = map(int, input().split())

    arr[a].extend([b])
    arr[a].sort()
    arr[b].extend([a])
    arr[b].sort()

DFS(1)

print(visit.count(1) - 1)