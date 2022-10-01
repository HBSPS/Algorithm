# 18258 큐 2

# 덱 사용
    # 각 입력에 대하여 배열로 입력 받는다 -> 함수와 값을 알기 위해
    # 덱을 사용하는 이유는 문제의 설명에서 각 연산의 시간 복잡도를 O(1)로 만들어야 한다고 했기 때문
        # 배열에서 pop(0)을 하게 되면 시간 복잡도 O(n), 덱에서 popleft()를 하게 되면 시간 복잡도 O(1)

# 명령의 수가 2,000,000이므로 sys 사용

import sys
from collections import deque

N = int(input())

dq = deque()

for i in range(N):
    tmp = sys.stdin.readline().split()

    if tmp[0] == "push":
        dq.append(tmp[1])
    elif tmp[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif tmp[0] == "size":
        print(len(dq))
    elif tmp[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])