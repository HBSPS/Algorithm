import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a = list(map(int, input().split()))

Min = 0
Max = max(a)

while Min <= Max:
    Mid = (Min + Max) // 2

    total = 0

    for i in a:
        if i > Mid:
            total = total + (i - Mid)

        if total > M: # 목표 량을 넘었을 경우 break를 한다. 백준에서 안하면 시간초과 발생. 이 코드 없이 pypy3로 제출하면 통과
            break
    
    if total >= M:
        Min = Mid + 1
    else:
        Max = Mid - 1

print(Max)