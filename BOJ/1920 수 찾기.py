N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

C = []

for i in range(M):
    C.append(0)

A.sort()

for i in range(M):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == B[i]:
            C[i] = 1
            break
        elif A[mid] > B[i]:
            end = mid - 1
        else:
            start = mid + 1

for i in C:
    print(i)