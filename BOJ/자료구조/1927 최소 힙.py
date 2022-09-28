# 1927 최소 힙

# 분류는 우선순위 큐 라고 되어있고 문제에서도 최소 힙이라고 한다
# 힙을 사용하므로 dq를 사용

# 비어있는 큐에서 요소를 뽑게되면 에러가 발생한다 -> try except문을 사용해서 문제의 조건에 맞는 출력을 해야한다

# dq의 최소값에 접근하기 위해 min(dq)를 사용

########

# 위의 방식으로 진행하니 시간초과 발생 -> 단순히 dq를 이용한 연산으로는 시간초과 발생 -> 최소 힙의 기본 원리인 완전 이진트리 사용해야 할 듯 (시간 복잡도: log(N))

# 부모노드의 index = N이라 할 때(루트 노드의 index는 1부터 시작), 왼쪽 자식의 index = 2N / 오른쪽 자식의 index = 2N + 1
    # ex) 부모노드 index = 2 / 왼쪽 자식 = 4, 오른쪽 자식 = 5
        #           1
        #       2       3
        #     4   5   6   7

# 파이썬에는 heapq라는 모듈이 있다
    # heapq를 사용하면 최소 힙과 최대 힙을 구할 수 있다
    # heappush(heap, item) -> heap에 item을 push(넣어)하는데 최소 힙의 규칙을 유지한다
    # heappop(heap) -> heap에서 최소값을 제거하고 반환한다

    # heapq에는 최대 힙을 제공하지 않는다
        # heapq를 사용해 최대 힙을 구하기 위해서는 heapq에 들어가는 값을에 -를 붙여 음수로 만들면 된다
        # ex) 5, 1, 2가 있다면 음수로 만들어 -5, -1, -2가 된다 -> 이 값을 가지고 최소 힙을 구하게 되면 -5가 루트 노드가 된다 -> heapq를 이용해 최소 힙을 구한 후 양수로 바꾸면 된다

import sys
import heapq

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    num = int(sys.stdin.readline())
    
    if num == 0:
        try:
            print(heapq.heappop(arr))
        except:
            print(0)
    else:
        heapq.heappush(arr, num)