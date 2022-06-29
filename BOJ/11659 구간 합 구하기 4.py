import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a = list(map(int, input().split()))

c = [0]

for i in range(N):
    c.append(c[i] + a[i])

for t in range(M):
    i, j = map(int, input().split())

    print(c[j] - c[i-1])