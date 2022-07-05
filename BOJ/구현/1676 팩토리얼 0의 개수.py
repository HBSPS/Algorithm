N = int(input())

total = 1

for i in range(1, N+1):
    total = total * i

l = list(map(int, str(total)))

cnt = 0

for _ in range(len(l)):
    tmp = l.pop()

    if tmp != 0:
        break
    else:
        cnt += 1

print(cnt)