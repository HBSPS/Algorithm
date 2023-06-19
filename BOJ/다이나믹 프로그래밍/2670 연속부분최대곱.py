# 2670 연속부분최대곱

""" arr = []

N = int(input())

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    dp[1][i] = eval(input())

for window in range(2, N+1):
    for i in range(window, N+1):
        dp[window][i] = round(dp[window-1][i-1] * dp[1][i], 3)

answer = 0
for row in dp:
    for item in row:
        if answer < item:
            answer = item

print(answer) """

N = int(input())

arr = [float(input()) for _ in range(N)]

for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1] * arr[i])

# print(round(max(arr), 3))
print('%0.3f' % max(arr))