# 1158 요세푸스 문제

# 덱을 생성하여 K만큼 회전 시킨 뒤 popleft

from collections import deque

N, K = map(int, input().split())

dq = deque()
answer = []

for i in range(1, N+1):
    dq.append(i)

while(len(dq) != 0):
    dq.rotate(-(K-1))
    answer.append(dq.popleft())

print('<', end='')

for i in range(0, len(answer)-1):
    print(answer[i], end=', ')

print(answer[-1], end='')
print('>')