# 12847 꿀 아르바이트

# 일을 할 수 있는 기간만큼의 합을 구하고 합의 최댓값을 찾는 것
    # 누적합 사용 가능 -> 누적 합 사용하지 않고 일일이 계산하면 시간초과 발생

# start와 end를 설정하여 윈도우의 움직임을 표현
    # 새로운 배열에 넣어서 max를 하기보다는 그때그때 max_sum을 설정하고 새롭게 구해지는 값과 비교하여 max값 찾기

N, M = map(int, input().split())

arr = list(map(int, input().split()))

ans = []

tmp = 0
for i in range(M):
    tmp += arr[i]

start = 0
end = M
max_sum = tmp

while end < N:
    tmp = tmp - arr[start] + arr[end]
    max_sum = max(max_sum, tmp)
    start += 1
    end += 1

print(max_sum)