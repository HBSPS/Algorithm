# 11399 ATM

# 그리디 알고리즘 - 미래의 선택을 생각하지 않고 지금의 선택에서 최선의 선택을 하는 알고리짐

# 만약, 배열의 가장 큰 수가 앞에 있게 된다면 그 큰 수는 각 사람이 인출을 할 때 마다 더해지게 된다 -> 가장 큰 수가 여러번 더해진다 = 최소 시간이 아니다
# 따라서, 작은 수가 앞에 위치하도록 해야 여러번 더해지더라도 최소의 시간을 만들 수 있게 된다

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

arr = [0] + arr

ans = [0] * (N + 1)

for i in range(1, N+1):
    ans[i] = ans[i-1] + arr[i]

print(sum(ans))