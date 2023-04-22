# 1051 숫자 정사각형

N, M = map(int, input().split())

table = []

for _ in range(N):
    table.append(list(map(int, input())))

answer = 0

for i in range(N):
    for j in range(M):
        x = i
        y = j
        k = 0

        while x + k < N and y + k < M:
            if table[x][y] == table[x + k][y] and table[x][y] == table[x][y + k] and table[x][y] == table[x + k][y + k]:
                answer = max((k + 1) * (k + 1), answer)

            k += 1

print(answer)