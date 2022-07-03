N, K = map(int, input().split())

L = []

for i in range(N):
    L.append(int(input()))
    
start = 1
end = max(L)

while start <= end:
    mid = (end + start) // 2

    total = 0

    for i in L:
        total += (i // mid)
    
    if total >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)