# 11003 최솟값 찾기

# 우선순위 큐 사용
    # 슬라이딩 윈도우에 새로 들어오는 원소를 우선순위 큐에 추가
    # 윈도우 밖으로 나가게 되는 원소와 우선순위 큐의 첫 원소와 비교
        # 만약, 두 값이 같다면 우선순위 큐에서 해당 값 pop
        # 다르다면 여전히 윈도우의 최솟값은 우선순위 큐의 첫 원소

    # 해당 방법을 사용하는 경우, 윈도우 밖으로 나가는 원소가 우선순위 큐의 첫 원소와 같지 않은 경우 힙에서 제거되지 않는 문제 발생
        # 힙의 최솟값이 모두 pop되어 두번째 최솟값을 가져와야 하지만 해당 값이 이미 윈도우 바깥으로 나간 경우 이미 지나간 원소가 최솟값으로 설정되는 문제 발생
        # 위의 방식에서 각 원소의 index도 사용해야 한다

"""
import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))

heap = []
window = deque()
answer = []

for i in range(L):
    heapq.heappush(heap, [arr[i], i])
    window.append(arr[i])

    answer.append(heap[0][0])

for i in range(L, N):
    if window.popleft() == heap[0][0]:
        heapq.heappop(heap)
    while i - heap[0][1] > L:
        heapq.heappop(heap)
    window.append(arr[i])
    heapq.heappush(heap, [arr[i], i])

    answer.append(heap[0][0])

print(*answer)
"""

# 위의 방식을 사용하면 시간초과 발생
    # heappop과 heappush의 시간 복잡도는 O(logN)
        # 결과적으로 시간 복잡도를 O(1)로 만들어야 한다

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))

dq = deque()

for i in range(N):
    while dq and dq[-1][0] > arr[i]:
        dq.pop()
    while dq and i - dq[0][1] >= L:
        dq.popleft()
    dq.append([arr[i], i])
    
    print(dq[0][0], end=' ')