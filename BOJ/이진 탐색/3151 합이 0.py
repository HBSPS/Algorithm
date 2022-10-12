# 3151 합이 0

# 단순하게 생각하면 주어진 수 3개를 조합하여 0을 만들 수 있는 경우의 수를 구하는 문제

# 나중에 다시 풀어와야 됨

""" import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j] + arr[k] == 0:
                cnt += 1

print(cnt) """

# 위의 코드로는 시간초과
    # 3중 for문은 최악의 방법인듯...

# 다시 풀어봐야 됨...
    # Python3으로는 시간 초과 -> pypy3로는 통과

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

cnt = Counter(arr) # 배열의 원소를 key로 갖고 중복 원소의 갯수를 value로 갖는 dict

result = 0

for i, a in enumerate(arr):
    left = i+1
    right = N-1
    
    while left < right:
        tmp = arr[i] + arr[left] + arr[right]

        if tmp == 0: # 세 수의 합이 0이 되는 경우
            if arr[left] == arr[right]: # 왼쪽과 오른쪽이 같은 경우
                result += (right - left) # 해당 값의 범위를 결과에 더한다
            else: # 값이 서로 다른경우
                result += cnt[arr[right]]
            
            left += 1

        elif tmp > 0:
            right -= 1

        elif tmp < 0:
            left += 1

print(result)