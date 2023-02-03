# 1992 쿼드트리

# 흑백 영상을 압축
    # 분할정복 + 재귀 사용
    # 기준점은 왼쪽 위
        # 왼쪽 위를 기준으로 이동

N = int(input())

arr = []
answer = []

for _ in range(N):
    arr.append(list(map(int, input())))

def quadTree(N, x, y):
    base = arr[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if base != arr[i][j]:
                base = -1
                break

    if base == -1:
        answer.append('(')
        N = N // 2
        quadTree(N, x, y) # 왼쪽 위
        quadTree(N, x, y + N) # 오른쪽 위
        quadTree(N, x + N, y) # 왼쪽 아래
        quadTree(N, x + N, y + N) # 오른쪽 아래
        answer.append(')')
    elif base == 0:
        answer.append(0)
    else:
        answer.append(1)

quadTree(N, 0, 0)

for i in answer:
    print(i, end='')