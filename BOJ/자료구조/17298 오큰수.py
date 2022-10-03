# 17298 오큰수

# 오큰수 -> 수열의 각 원소에 대해 특정 원소의 오큰수는 오른쪽에 있으면서 해당 원소보다 큰 수 중에 가장 왼쪽에 있는 수

# 4, 3, 2가 있는 상황에서 9가 추가 되면 앞의 원소들의 오큰수는 모두 9가 된다
    # 스택 사용하여 배열을 비운다
    # 4, 3, 7, 2, 9의 순서라고 한다면 4, 3에 7이 추가되며 4, 3을 제거 + 7추가 -> [7]
        # 이후, 2추가 -> [7, 2] => 9가 오게 되면서 7, 2 제거 + 9 추가 -> [9]

# for문 중쳡으로 하게 되면 시간 복잡도의 상상으로 인한 시간초과 발생
    # 스택을 사용하되 인덱스를 넣는 방법? -> 이게 되네...

N = int(input())

arr = list(map(int, input().split()))

ans = [-1 for _ in range(N)]

stack = [0]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    
    stack.append(i)

for i in ans:
    print(i, end=" ")