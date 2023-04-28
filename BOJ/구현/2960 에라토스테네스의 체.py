# 2960 에라토스테네스의 체

N, K = map(int, input().split())

arr = [i for i in range(N+1)]

arr[1] = 0

def getAnswer(N, K, count):
    for i in range(N+1):
        tmp = i
        tmp_value = arr[i]

        if arr[tmp] != 0:
            while tmp <= N:
                if arr[tmp] != 0:
                    count += 1
                    if count == K:
                        return arr[tmp]

                    arr[tmp] = 0

                tmp += i

            arr[i] = tmp_value

print(getAnswer(N, K, 0))