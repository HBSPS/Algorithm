# 14912 숫자 빈도수

n, d = map(int, input().split())

arr = []

for i in range(1, n+1):
    i = str(i)
    arr.append(list(i))

count = 0

for number in arr:
    for digit in number:
        if digit == str(d):
            count += 1

print(count)