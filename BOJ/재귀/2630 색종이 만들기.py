# 2630 색종이 만들기

# 한 구역이 모두 같은 색으로 이루어져 있게 되거나, 한 칸이 되어 더이상 나눌 수 없을 때 까지

# 재귀함수를 돌리며 각 색에 대한 Count를 해야 하므로 global을 사용하여 변수를 선언한다

# 각 구역에 대한 x, y좌표 => x,y / x+N/2, y / x, y+N/2 / x+N/2, y+N/2
    # 따라서, 현재 상태에서 색이 다른 부분이 있다면 각 영역에 대해 재귀함수 실행
    # 우선 현재 구역의 제일 첫 부분의 색을 임시로 지정하고, 구역을 탐색하며 색이 다른 부분이 있다면 재귀함수를 돌린다.
        # 재귀함수가 실행된다면 return을 통해 count가 되지 않게 해야 한다

# 추가사항 : Slice 재귀를 돌리며 인자로 N/2를 넘겨주게 되면 타입 오류 발생
    # N/2는 float 형이기 때문에 N//2를 통해 int형으로 만들어야 한다

import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

Wcnt = Bcnt = 0

def Slice(x, y, N):
    global Wcnt, Bcnt

    tmp = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp != arr[i][j]:
                Slice(x, y, N//2)
                Slice(x+N//2, y, N//2)
                Slice(x, y+N//2, N//2)
                Slice(x+N//2, y+N//2, N//2)
                return

    if tmp == 1:
        Bcnt += 1
    else:
        Wcnt += 1

Slice(0, 0, N)
print(Wcnt)
print(Bcnt)