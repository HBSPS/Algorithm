# 1748 수 이어 쓰기 1

# 1 ~ 9 -> 1자릿 수 => 합: 9
# 10 ~ 99 -> 2자릿 수 => 합: 90 * 2 = 180 = 9 * 20
    # 1 ~ 99 => 합: 189
# 100 ~ 999 -> 3자릿 수 => 합: 900 * 3 = 2700 = 9 * 300

N = int(input())

length = len(str(N))

answer = 0

if N < 10:
    print(N)
elif 10 <= N and N <= 99:
    print(9 + (N-9) * 2)
else:
    answer = 189

    for i in range(3, length):
        tmp = 9
        answer += tmp * i * (10 ** (i -1))

    answer += ((N - (10 ** (length-1)) + 1) * length)

    print(answer)