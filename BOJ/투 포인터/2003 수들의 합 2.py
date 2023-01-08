# 2003 수 들의 합 2

# A[i] ~ A[j]까지의 합이 M이 되는 경우를 구해야 한다 -> 시적점 i를 기준으로 j까지 더하는 과정
    # 따라서, 투포인터
# 합이 M을 넘으면 continue
    # 합과 M이 같으면 count 증가

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
tmp = 0

for i in range(N-1):
    if arr[i] == M:
        count += 1
        continue
    tmp = arr[i]
    for j in range(i+1, N):
        tmp += arr[j]
        if tmp == M:
            count += 1
            break
        elif tmp > M:
            break

print(count)
'''
# 위의 방식은 시간초과
    # 단순 for문 중첩으로는 시간초과 발생

# 투 포인터 사용을 결정했다면 단순히 for문을 중첩하는 것이 아니라 '투 포인터'에 집중하여 start와 end를 각각 지정하는 것이 필요
    # 원하는 값보다 포인터 사이의 값들의 합이 작다면 오른쪽 포인터 한 칸 이동
    # 원하는 값보다 포인터 사이의 값들의 합이 크다면 왼쪽 포인터 한 칸 이동
    # 원하는 값과 포인터 사이의 값들의 합이 같은 경우 오른쪽 포인터 한 칸 이동

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
count = 0

while left <= right and right <= N:
    tmp = arr[left:right]
    total = sum(tmp)

    if total == M:
        count += 1
        right += 1
    elif total > M:
        left += 1
    else:
        right += 1

print(count)