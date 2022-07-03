from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

dq = deque()

for i in range(N):
    tmp = list(map(str, input().split()))

    if tmp[0] == 'push_back':
        dq.append(tmp[1])
    elif tmp[0] == 'push_front':
        dq.appendleft(tmp[1])
    elif tmp[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif tmp[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif tmp[0] == 'size':
        print(len(dq))
    elif tmp[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])