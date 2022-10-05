# 14465 소가 길을 건너간 이유

# 연속된 갯수의 가로등이 되기 위해서 몇개의 가로등을 수리해야 하는가? -> 슬라이딩 윈도우
    # 멀쩡한 가로등 = 1 / 고장난 가로등 = 0으로 배열을 만들어 1의 갯수가 가장 많도록

N, K, B = map(int, input().split())

arr = [1 for i in range(N)]

ans = []

for _ in range(B):
    arr[int(input())-1] = 0

tmp = 0
for i in range(K):
    tmp += arr[i]

start = 0
end = K
max_sum = tmp

while end < N:
    tmp = tmp - arr[start] + arr[end]
    max_sum = max(max_sum, tmp)
    start += 1
    end += 1

print(K - max_sum)