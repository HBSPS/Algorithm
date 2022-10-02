# 24416 알고리즘 수업 - 피보나치 수 1

# 피보나치 수 -> 문제에 나온 대로 구현하기만 하면 됨

# Python3로 제출할 경우 시간초과 -> pypy3로 제출해야 함

N = int(input())

def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)

def fibonacci(N):
    arr = [0]*(N+1)
    arr[1] = arr[2] = 1
    cnt = 0

    for i in range(3, N+1):
        cnt += 1
        arr[i] = arr[i-1] + arr[i-2]

    return cnt

print(fib(N), fibonacci(N))