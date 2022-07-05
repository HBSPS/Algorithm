from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    a = deque(list(map(int, input().split()))) # 우선 순위

    b = deque() # index

    for i in range(N):
        b.append(i)

    cnt = 0
        
    while 1:
        if a[0] != max(a):
            a.rotate(-1)
            b.rotate(-1)
        else:
            if b[0] == M:
                cnt += 1
                break
            else:
                a.popleft()
                b.popleft()

                cnt += 1
        
    print(cnt)