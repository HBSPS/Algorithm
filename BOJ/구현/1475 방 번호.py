# 1475 방 번호

N = list(map(int, input()))

count = 0

table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in N:
    if number == 6 or number == 9:
        count += 1
    else:
        table[number] += 1

if count % 2 == 0:
    count = count // 2
else:
    count = count // 2 + 1

print(max(max(table), count))