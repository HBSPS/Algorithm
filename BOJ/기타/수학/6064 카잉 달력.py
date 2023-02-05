# 6064 카잉 달력

# 중국인의 나머지 정리
    # 연립 합동식의 해가 존재한다 + 그 해가 유일하다
    # 예시
        # x를 3으로 나누면 나머지가 1이다
        # x를 5으로 나누면 나머지가 1이다
        # x를 15로 나눈 나머지는? => 1이라는 것을 증명하는 것이 중국인의 나머지 정리

# 몇 년 인지를 구하는 문제
    # 카잉 달력의 끝은 N과 M의 최소 공배수
    # x는 구하고자 하는 연도를 M으로 나눈 나머지
    # y는 구하고자 하는 연도를 N으로 나눈 나머지
    # 구하고자 하는 연도 a에 대해
        # (a - x) % M = 0
        # (a - y) % N = 0
        # a = x + 여러개의 M
        # 따라서 (x + 여러개의 M - y) % N = 0

import math

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    check = 0

    while x <= math.lcm(M, N):
        if (x - y) % N == 0:
            print(x)
            check = 1
            break
        x += M
    
    if check == 0:
        print(-1)