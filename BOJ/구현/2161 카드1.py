# 2161 카드1

from collections import deque

N = int(input())

dq = deque()

for i in range(1, N + 1):
    dq.append(i)

while True:
    if len(dq) == 1:
        print(dq.pop(), end=' ')
        break

    print(dq.popleft(), end=' ')

    dq.append(dq.popleft())