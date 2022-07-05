N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

c = []

for i in range(M):
    c.append(0)

a.sort()


for i in range(M):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == b[i]:
            c[i] = 1
            break
        elif a[mid] < b[i]:
            start = mid + 1
        else:
            end = mid - 1

for i in c:
    print(i, end=" ")