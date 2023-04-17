# 16395 파스칼의 삼각형

N, M = map(int, input().split())

dp = [[0] for _ in range(N+1)]

if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    dp[1].append(1)
    dp[2].append(1)
    dp[2].append(1)
    
    for i in range(3, N+1):
        for j in range(1, i+1):
            if j == 1 or j == i:
                dp[i].append(1)
            else:
                dp[i].append(dp[i-1][j] + dp[i-1][j-1])

    print(dp[N][M])