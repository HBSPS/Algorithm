import sys

input = sys.stdin.readline

M = int(input())

s = set()

for i in range(M):
    N = input().strip().split()

    if len(N) == 1:
        if N[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    a, b = N[0], int(N[1])

    if a == "add":
        s.add(b)
    elif a == "remove":
        s.discard(b)
    elif a == "check":
        if b in s:
            print(1)
        else:
            print(0)
    elif a == "toggle":
        if b in s:
            s.discard(b)
        else:
            s.add(b)