# 2491 수열

# 현재 위치 까지의 가장 긴 증가 또는 감소하는 부분 수열을 dp로 저장
    # 증가하는 경우와 감소하는 경우 각각의 dp를 구한 뒤, 두 dp 배열에서 가장 큰 값을 출력

N = int(input())

arr = list(map(int, input().split()))

dp_up = [1 for _ in range(N)]
dp_down = [1 for _ in range(N)]

for i in range(1, N):
    if arr[i-1] <= arr[i]:
        dp_up[i] = dp_up[i-1] + 1
    if arr[i-1] >= arr[i]:
        dp_down[i] = dp_down[i-1] + 1

print(max(max(dp_up), max(dp_down)))