# 9507 Generations of Tribbles

T = int(input())

dp = [1, 1, 2, 4] + [0 for _ in range(64)]
answer = []

for _ in range(T):
    N = int(input())
    
    if N < 3:
        answer.append(dp[N])
        continue

    if dp[N] != 0:
        answer.append(dp[N])
    else:
        for i in range(3, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

        answer.append(dp[N])

for i in answer:
    print(i)