# 11286 절댓값 힙

# 우선순위 큐를 사용
    # 절댓값이 가장 작은 숫자부터 출력
    # 만약, 절댓값이 같다면 작은 숫자부터 출력
    # 비어있는 경우 0을 출력

# 우선순위 큐에 절댓값과 실제 값을 갖도록 저장
    # [절댓값, 실제값]

import heapq
import sys

input = sys.stdin.readline

N = int(input())

arr = []
answer = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if len(arr) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(arr)[1])
        continue

    if x < 0:
        heapq.heappush(arr, [-x, x])
    else:
        heapq.heappush(arr, [x, x])

for i in answer:
    print(i)