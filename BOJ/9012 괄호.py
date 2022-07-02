from collections import deque

N = int(input())

ans = []

for i in range(N):
    a = deque(input())

    L = 0

    for j in range(len(a)):
        tmp = a.popleft()

        if tmp == '(':
            L += 1
        else:
            L -= 1
        
        if L < 0:
            break
    
    if L == 0:
        ans.append('YES')
    elif L > 0:
        ans.append('NO')
    elif L < 0:
        ans.append('NO')
            
for i in ans:
    print(i)