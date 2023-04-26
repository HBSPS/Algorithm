# 2167 2차원 배열의 합

''' 시간초과
N, M = map(int, input().split())

table = [[0 for _ in range(M+1)]]

answer = []

for _ in range(N):
    table.append([0] + list(map(int, input().split())))

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())

    tmp = 0

    for dx in range(i, x + 1):
        for dy in range(j, y + 1):
            tmp += table[dx][dy]

    answer.append(tmp)

for i in answer:
    print(i)
'''

# 일반적인 방법으로는 시간 초과가 발생하므로 누적합(DP)을 이용해서 풀이해야 한다
    # 특정 위치까지의 누적합을 이용해 dp 테이블을 초기화 할 때, (특정 위치의 실제 값 + dp의 왼쪽 값 + dp의 위쪽 값 - dp의 왼쪽 위의 값)으로 초기화 해야한다
    
N, M = map(int, input().split())

dp = [[0] * (M + 1) for _ in range(N + 1)]
table = []

answer = []

for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = table[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())

    answer.append(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

for i in answer:
    print(i)