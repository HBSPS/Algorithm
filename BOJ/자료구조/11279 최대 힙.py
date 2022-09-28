# 백준 11279 최대 힙

# 최소 힙을 구하는 방법과 동일하게 heapq 모듈을 사용한다
# 단, heapq는 최소 힙을 구하기 떄문에 최대 힙을 구하기 위해서는 모든 수에 음수로 만들어 최소 힙을 구하듯이 구해야 한다 -> 출력 단계에서 음수를 양수로 다시 바꾸면 됨

import sys
import heapq

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    tmp = -int(sys.stdin.readline())

    if tmp == 0:
        try:
            print(-heapq.heappop(arr))
        except:
            print(0)
    else:
        heapq.heappush(arr, tmp)