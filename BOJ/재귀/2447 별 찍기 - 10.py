# 2447 별 찍기 - 10

# 같은 형태의 반복 -> 재귀 사용

# 전체 크기 N(3의 배수)을 받아서, 3으로 나누며 재귀
    # 만약, 재귀 도중 N = 3이 된다면 별을 찍는다

N = int(input())

arr= ["***", "* *", "***"] # 기본 별 찍기 배열

def Star(N, arr):
    ans = [] # 매 반복마다 새롭게 배열을 선언

    if N == 3:
        return arr # N = 3이 된다면 결과 반환과 함께 재귀 종료
    else:
        for i in arr:
            ans.append(i*3) # 윗 줄
        for i in arr:
            ans.append(i + " "*len(arr) + i) # 중간 줄
        for i in arr:
            ans.append(i*3) # 아랫 줄

        # 결국, ans는 N이 9, 27, 81...로 증가함에 따라 N X N 크기의 2차원 배열을 갖게 된다
        
        return Star(N/3, ans) # N은 사실상 재귀의 반복 횟수를 제한하기 위한 것

ans = Star(N, arr)

# N이 2차원 배열이기 때문에 for문을 통해 print하면 된다
for i in ans:
    print(i)