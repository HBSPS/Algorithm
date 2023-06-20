# 1417 국회의원 선거

# 가장 많은 표를 1번으로 옮기는 과정을 반복
    # 그리디 알고리즘

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

if N == 1:
    print(0)
else:
    A = arr[0]
    arr = arr[1:]
    count = 0

    while A <= max(arr):
        arr.sort(reverse=True)
        arr[0] -= 1
        A += 1
        count += 1

    print(count)