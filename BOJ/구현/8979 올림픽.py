# 8979 올림픽

N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())) + [-1])

arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

arr[0][4] = 1
rank = 1

for i in range(1, N):
    if arr[i-1][1] == arr[i][1] and arr[i-1][2] == arr[i][2] and arr[i-1][3] == arr[i][3]:
        arr[i][4] = arr[i-1][4]
        rank += 1
    else:
        rank += 1
        arr[i][4] = rank

for item in arr:
    if item[0] == K:
        print(item[4])
        break