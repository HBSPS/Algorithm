# 15961 회전 초밥

# 2531 회전 초밥 문제와 동일한 문제
    # 단, 15961 회전 초밥의 경우 2531 회전 초밥보다 N의 범위가 넓다
    
    # 2531번의 코드를 그대로 제출 -> 시간초과
        # 시간초과의 원인 -> 아마도 회전을 구현하기 위해 같은 리스트 두 개를 연결한 것
        # 같은 리스트의 연장때문에 중복되는 부분이 발생
            # 연속으로 먹는 초밥의 수 만큼만 배열에 추가

from collections import defaultdict
import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]

arr.extend(arr[:(k-1)])

start = 0
end = 0

sushi_dict = defaultdict(int)

sushi_dict[c] += 1

while end < k:
    sushi_dict[arr[end]] += 1
    end += 1

result = 0

while end < len(arr):
    result = max(result, len(sushi_dict))

    sushi_dict[arr[start]] -= 1
    if sushi_dict[arr[start]] == 0:
        del sushi_dict[arr[start]]

    sushi_dict[arr[end]] += 1
    
    start += 1
    end += 1

print(result)