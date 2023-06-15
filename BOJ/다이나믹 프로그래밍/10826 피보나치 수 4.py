# 10826 피보나치 수 4

N = int(input())

dp = [0, 1] + [0 for _ in range(2, N+1)]

if N < 2:
    print(dp[N])
else:
    for i in range(2, N+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[N])