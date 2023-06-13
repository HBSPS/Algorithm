# 1769 3의 배수

# 시간 초과 발생
    # 원인: int -> str로 변환하는 str()은 O(logn)의 사간복잡도

'''
X = int(input())

if X < 10:
    print(0)
    if X % 3 == 0:
        print('YES')
    else:
        print('NO')
else:
    X = list(map(int, str(X)))

    Y = sum(X)
    count = 1

    while Y > 9:
        Y = list(map(int, str(Y)))
        Y = sum(Y)
        count += 1

    print(count)
    if Y % 3 == 0:
        print('YES')
    else:
        print('NO')
'''
def check(X, count):
    if len(X) == 1:
        if int(X) % 3 == 0:
            print(count)
            print('YES')
            return
        else:
            print(count)
            print('NO')
            return
        
    else:
        tmp = 0
        for i in X:
            tmp += int(i)
        X = str(tmp)
        count += 1
        check(X, count)

check(input(), 0)