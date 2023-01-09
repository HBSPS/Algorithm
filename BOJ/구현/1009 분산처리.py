# 1009 분산처리

# a^b의 형태로 주어지기 때문에 연산을 먼저 수행
    # 연산의 결과를 10으로 나눈 나머지

'''
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    total = a ** b

    print(total % 10)
'''

# 위의 코드는 시간 초과
    # 모든 숫자를 제곱 처리 하는 것이 아니라 마지막 숫자만 제곱하는 방법을 사용하는 것도 좋을 듯
        # 컴퓨터의 갯수는 10개 이므로 결국 마지막 자릿수가 마지막 데이터를 처리하는 컴퓨터
        # 0 ~ 9에 해당하는 제곱수들을 미리 구한다

# 0: 1
# 1: 1
# 2: 2, 4, 8, 6
# 3: 3, 9, 7, 1
# 4: 4, 6
# 5: 5
# 6: 6
# 7: 7, 9, 3, 1
# 8: 8, 4, 2, 6
# 9: 1, 9

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a ** 2) % 10)
        else:
            print(a % 10)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        print((a ** b) % 10)