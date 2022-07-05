N, M = map(int, input().split())

dict = {}

ans = []

for _ in range(N):
    a, b = map(str, input().split())

    dict[a] = b

for _ in range(M):
    tmp = input()

    ans.append(dict[tmp])

for i in ans:
    print(i)