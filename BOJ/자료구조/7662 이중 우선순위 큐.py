# 7662 이중 우선순위 큐

# D 1 -> 큐에서 최댓값 제거 / D -1 -> 큐에서 최솟값 제거 / I num -> 큐에 num 추가
    # 큐에 남아있는 값 중 최댓값과 최솟값을 출력 / 비어있다면 EMPTY

# 우선순위에 대해 값을 삭제하므로 우선순위 큐 -> 최대 힙 / 최소 힙
    # heapq 사용 -> 단, heapq는 최소 힙만 제공
        # 최대 힙과 최소 힙을 구현하여 연산을 수행

# 문제의 핵심은 최대 힙과 최소 힙을 구현하여 연산을 하게 되는데, 이 두 힙을 어떻게 하나로 합치는 것인지다

import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())

    arr1 = [] # 최소 힙 -> 연산이 끝난 후 최소 값을 반환하게 되면 전체 배열의 최솟값이 된다
    arr2 = [] # 최대 힙 -> 연산이 끝난 후 최대 값을 반환하게 되면 전체 배열의 최댓값이 된다
    visit = [0 for _ in range(K)] # 두 힙을 연동시키기 위한 것

    for i in range(K):
        tmp = input().split()
        tmp[1] = int(tmp[1])

        if tmp[0] == "I":
            heapq.heappush(arr1, (tmp[1], i))
            heapq.heappush(arr2, (-tmp[1], i))
            visit[i] = 1

        else:
            if tmp[1] == -1: # 최소 힙
                while arr1 and not visit[arr1[0][1]]: # 최소 힙에 원소가 존재하고 최소 노드에 방문하지 않았다면 -> 최소 힙 제거 반복
                    heapq.heappop(arr1)
                if arr1:
                    visit[arr1[0][1]] = 0
                    heapq.heappop(arr1)
            else:
                while arr2 and not visit[arr2[0][1]]:
                    heapq.heappop(arr2)
                if arr2:
                    visit[arr2[0][1]] = 0
                    heapq.heappop(arr2)
    
    while arr1 and not visit[arr1[0][1]]:
        heapq.heappop(arr1)
    while arr2 and not visit[arr2[0][1]]:
        heapq.heappop(arr2)

    if not arr1 or not arr2:
        print("EMPTY")
    else:
        print(-arr2[0][0], arr1[0][0], sep=" ")