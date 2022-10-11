# 2531 회전초밥

# 문제에 따르면 연속을 정해진 갯수의 초밥을 먹고, 쿠폰까지 사용할 때 최대로 먹을 수 있는 초밥의 가짓수를 출력하는 문제이다
    # 같은 초밥을 두 번 먹는 경우 가짓수는 한가지로 판단 -> 몇개를 먹던 한개 => 딕셔너리
    # 모든 경우에 대해 판단해야 하므로 브루트포스 -> 시간초과 가능성 O
    # 원형으로 회전한다고 했으니 회전큐를 적용할 수 있으나, 단순하게 같은 배열 두개를 이어붙이는 것으로 구현가능

from collections import defaultdict
import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]

arr.extend(arr)

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