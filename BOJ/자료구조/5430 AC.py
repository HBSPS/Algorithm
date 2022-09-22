# 5430 AC

# R의 개수가 짝수인 경우 배열의 원상 복귀 -> 굳이 수행할 필요 없음
# R의 개수가 홀수인 경우 배열의 맨 끝에서 꺼내는 것과 같음

# 따라서, R의 개수가 짝수일 때 -> popleft() / R의 개수가 홀수일 때 -> pop()

from collections import deque

T = int(input()) # 테스트 케이스 개수

for i in range(T):
    fnArr = list(input()) # 수행할 함수

    N = int(input()) # 배열에 들어있는 수의 개수

    arr = input()[1:-1].split(",") # 사용자 입력 배열

    dq = deque(arr) # 사용자 입력 덱으로 전환

    # N = 0인 경우 빈 배열
    if N == 0:
        dq = []

    # R의 개수
    countR = 0
    # error인 경우 선별용
    ans = 0

    # 수행할 함수에 대한 반복문
    for j in fnArr:
        # R을 수행하는 경우 R의 카운트 1 증가
        if j == "R":
            countR += 1
        # D를 수행하는 경우
        elif j == "D":
            # dq의 길이가 0인 경우
            if len(dq) == 0:
                print("error") # error 출력 후
                ans = 1
                break # 반복문 종료
            else:
                # R의 개수가 짝수인 경우
                if countR % 2 == 0:
                    dq.popleft()
                # R의 개수가 홀수인 경우
                else:
                    dq.pop()

    # 반복문이 중간에 종료되지 않았고
    if ans == 0:
        # R의 개수가 짝수인 경우 그대로 출력
        if countR % 2 == 0:
            print("[" + ",".join(dq) + "]")
        # R의 개수가 홀수인 경우 뒤집어서 출력
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")