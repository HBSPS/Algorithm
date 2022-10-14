# 11727 2Xn 타일링 2

# 이전의 연산 결과를 이후에도 사용 -> DP를 이용
    # 점화식 찾아서 구현만 하면 됨
    # 중요한 것은 DP를 이용해 이전의 계산 결과를 저장하고 사용해서 시간을 줄이는 것

N = int(input())

ans = [0, 1, 3, 5] + [0 for _ in range(N-3)] # N+1의 길이를 갖는 배열을 0으로 초기화 + 1, 2, 3의 경우는 사전에 값을 정의 (index를 1부터 시작하도록 첫 값은 0 삽입)

if N < 4:
    print(ans[N])
else:
    for i in range(4, N+1):
        ans[i] = ans[i-1] + 2 * ans[i-2]

    print(ans[N]%10007)