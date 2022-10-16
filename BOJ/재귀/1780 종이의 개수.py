# 1780 종이의 개수

# 한 변이 3의 제곱수로 되어 있는 정사각형을 자른다
    # 만약, 자른 정사각형에 모두 같은 숫자가 있다면 count + 1
        # 자른 정사각형의 숫자가 모두 같지 않다면 다시 정사각형을 9등분

# 우선 잘린 정사각형 속 다른 요소가 있는지 검사
    # 만약, 정사각형의 숫자가 다르다면 9등분을 하기 위해 각 사각형의 좌측 상단 요소를 기준으로 N//3, 2 * N//3 씩 더해주며 재귀 방식 사용

N = int(input())

arr = []

count = {-1: 0, 0: 0, 1: 0}

for _ in range(N):
    arr.append(list(map(int, input().split())))

def Slice(x, y, N):
    tmp = arr[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp != arr[i][j]:
                Slice(x, y, N//3)
                Slice(x+N//3, y, N//3)
                Slice(x+2*N//3, y, N//3)

                Slice(x, y+N//3, N//3)
                Slice(x+N//3, y+N//3, N//3)
                Slice(x+2*N//3, y+N//3, N//3)

                Slice(x, y+2*N//3, N//3)
                Slice(x+N//3, y+2*N//3, N//3)
                Slice(x+2*N//3, y+2*N//3, N//3)
                return
        
    if tmp == 0:
        count[0] += 1
    elif tmp == 1:
        count[1] += 1
    else:
        count[-1] += 1

Slice(0, 0, N)
for i in range(-1, 2):
    print(count[i])