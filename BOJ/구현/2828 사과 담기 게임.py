# 2828 사과 담기 게임

N, M = map(int, input().split())
j = int(input())

arr = []
current = 1
answer = 0

for _ in range(j):
    arr.append(int(input()))

for item in arr:
    if current <= item and current + (M-1) >= item:
        continue
    elif current > item:
        answer += abs(item - current)
        current = item
    else:
        answer += item - (M-1) - current
        current = item - (M-1)

print(answer)