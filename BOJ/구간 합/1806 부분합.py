# 1806 부분합

# 부분합을 구하는 것. 하지만, 부분합을 구하는 길이는 정해져 있지 않으므로 전체를 탐색해야 한다
    # 투포인터를 이용해 각 케이스에 대해 브루트포스

# 만약, 부분합이 S보다 작다면 end를 증가
    # end를 증가시키는 도중 S이상이 된다면 start를 1증가
    # S 이상이 되는 경우의 end-start를 배열에 넣고 최소를 출력

# 그냥 배열에서 최솟값을 출력하면 ValueError 발생
    # 부분합이 S 이상을 만들 수 없는 경우, 비어있는 배열이기 때문에 min(ans)를 하게 되면 ValueError 발생
        # try except문을 이용해 S이상을 만들 수 없는 경우 0을 출력하도록 한다

import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

ans = []

end = 0
tmp_sum = 0

for start in range(N):
    while tmp_sum < S and end < N:
        tmp_sum += arr[end]
        end += 1
    
    if tmp_sum >= S:
        ans.append(end-start)
    tmp_sum -= arr[start]

try:
    print(min(ans))
except:
    print(0)