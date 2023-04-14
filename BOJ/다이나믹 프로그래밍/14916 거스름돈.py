# 14916 거스름돈

## 수학으로 풀이 ##
"""
N = int(input())

answer = 0

while True:
    if N % 5 == 0:
        answer += N // 5
        break
    else:
        N -= 2
        answer += 1

    if N < 0:
        break

if N < 0:
    print(-1)
else:
    print(answer)
"""
##################

### DP로 풀이 ####

# 특정 금액을 줄 수 있는 방법은 2원이 추가되거나 5원이 추가되거나 둘 중 하나
    # 따라서, N만큼의 거스름돈을 만들 수 있는 최소 갯수는 dp[N-5], dp[N-2] 중 작은 값에 1을 더한 것과 같다
    # 9이상의 수는 모두 5와 2의 조합으로 만들 수 있지만 그렇지 않은 부분 (1 ~ 8)에 해당하는 값은 미리 초기화 해줘야 한다

N = int(input())

dp = [-1] * (N+1)

dp[2]=1
dp[4]=2
dp[5]=1
dp[6]=3
dp[7]=2
dp[8]=4

for i in range(9, N+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[N])
##################