from collections import deque

N, M = map(int, input().split())

dq = deque()

ans = []

for i in range(N):
    dq.append(i + 1)

for i in range(N):
    dq.rotate(-M)

    tmp = dq.pop()

    ans.append(tmp)

print("<", end="")
for i in range(N - 1):
    print(ans[i], end=", ")
print(ans[-1], end="")
print(">")