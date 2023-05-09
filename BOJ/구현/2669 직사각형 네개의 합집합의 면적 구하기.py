# 2669 직사각형 네개의 합집합의 면적 구하기

table = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    ldx, ldy, rux, ruy = map(int, input().split())

    for x in range(ldx, rux):
        for y in range(ldy, ruy):
            table[x][y] = 1

count = 0

for row in table:
    for item in row:
        if item == 1:
            count += 1

print(count)