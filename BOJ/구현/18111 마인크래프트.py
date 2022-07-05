import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

ans = 99999999999999999999999999999999999999 # 초기 시간을 매우 크게 설정하여 비교할 수 있도록 한다
height = 0

for i in range(257):
    max = 0
    min = 0

    for j in range(N):
        for k in range(M):
            if table[j][k] < i:
                min += (i - table[j][k]) # i층으로 맞춘다고 할 때, 필요한 블록의 개수
            else:
                max += (table[j][k] - i) # i층으로 맞춘다고 할 때, 부숴야 하는 블록의 개수
    
    inven = max + B

    if inven < min: # i층을 만들기 위해 i층 위의 모든 블록을 부수고 처음 B개의 블록을 더해도 모든 땅을 고르게 만들지 못하는 경우
        continue

    time = 2 * max + min # max개 만큼 부수고, min개 만큼 쌓으므로

    if time <= ans: # 최소 시간과 같거나 작으면
        ans = time
        height = i # i는 오름차순 이므로 같은 시간이 걸리더라도 i(높이)는 커지게 된다

print(ans, height)