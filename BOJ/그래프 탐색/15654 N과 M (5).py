# 15654 N과 M (5)

# N개의 자연수 중, M개를 고른 수열
    # 단, 사전 순으로 증가하는 순서로 출력

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

visited = [False] * N
answer = []

def DFS():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            DFS()
            visited[i] = False
            answer.pop()

DFS()