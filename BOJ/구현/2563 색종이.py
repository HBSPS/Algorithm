# 2563 색종이

N = int(input())

table = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            table[i][j] = 1

count = 0

for row in table:
    for j in row:
        if j == 1:
            count += 1

print(count)