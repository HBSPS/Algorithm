from collections import deque

N = int(input())

a = deque()

for i in range(N):
    a.append(i+1)

k = 1

while len(a) != 1:
    if (k % 2 != 0):
        a.popleft()
    else:
        j = a.popleft()

        a.append(j)
    k += 1

ans = a.popleft()

print(ans)