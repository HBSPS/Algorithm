from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

A.sort()

A = deque(A)

dict = {}

for i in range(N):
    tmp = A.popleft()

    if tmp in dict:
        dict[tmp] += 1
    else:
        dict[tmp] = 1

ans = []

for i in B:
    if i in dict:
        ans.append(dict[i])
    else:
        ans.append(0)

for i in ans:
    print(i, end=" ")