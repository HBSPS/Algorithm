# Four Squares

# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 효현할 수 있다

# N을 만들기 위해 필요한 제곱수들의 최소 갯수 출력
    # 그냥 루트 씌우는 것도 방법일듯...??
        # 위와 같이 그리디 알고리즘으로 해결하려 하면 반례가 있다
            # 12의 경우, 그리디 알고리즘으로는 9 + 1 + 1 + 1으로 갯수가 4가 나온다
            # 문제의 조건에 따르면 12 = 4 + 4 + 4로 갯수가 3이 나와야 한다
    # 따라서, 그리디 알고리즘이 아닌 DP를 사용해서 해결해야 한다

''' N = int(input())

arr = []

while N > 0:
    tmp = int(N **(1/2))

    N -= tmp ** 2
    
    arr.append(tmp)

arr = set(arr)
print(len(arr)) '''

N = int(input())

arr = [0] * (N+1)

k = 1
while k**2 <= N:
    arr[k**2] = 1
    k += 1

for i in range(1, N+1):
    if arr[i] != 0:
        continue

    j = 1
    while j*j <= i:
        if arr[i] == 0:
            arr[i] = arr[j*j] + arr[i - j*j]
        else:
            arr[i] = min(arr[i], arr[j*j] + arr[i - j*j])

        j += 1
        
print(arr[N])