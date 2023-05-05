# 2331 반복수열

import math

A, P = map(int, input().split())

arr = []
arr.append(A)

index = 1
while True:
    digits = (list(map(int, str(arr[index-1]))))

    tmp = 0
    for digit in digits:
        tmp += int(math.pow(digit, P))

    if tmp in arr:
        answer = arr[:arr.index(tmp)]
        print(len(answer))
        break
    else:
        arr.append(tmp)
        index += 1