# 11726 2Nn 타일링

# a[i] = a[i-2] + a[i-1] -> dp 사용

N = int(input())

if N < 4:
    arr = [0, 1, 2, 3]

    print(arr[N])
else:
    arr = [0, 1, 2, 3] + [0 for _ in range(4, N+1)]

    for i in range(4, N+1):
        arr[i] = arr[i-2] + arr[i-1]
    
    print(arr[N] % 10007)