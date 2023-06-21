# 10157 자리배정

C, R = map(int, input().split())
K = int(input())

table = [[0 for _ in range(C)] for _ in range(R)]

if K > C * R:
    print(0)
else:
    y = R-1
    x = 0
    index = 1
    check = False
    a = 0
    b = 0

    while index <= C * R:
        while y >= 0 and table[y][x] == 0:
            if index == K:
                a = y
                b = x
                check = True
                break
            table[y][x] = index
            y -= 1
            index += 1
        
        if check:
            break

        y += 1
        x += 1
        while x < C and table[y][x] == 0:
            if index == K:
                a = y
                b = x
                check = True
                break
            table[y][x] = index
            x += 1
            index += 1
        
        if check:
            break

        y += 1
        x -= 1
        while y < R and table[y][x] == 0:
            if index == K:
                a = y
                b = x
                check = True
                break
            table[y][x] = index
            y += 1
            index += 1
        
        if check:
            break

        y -= 1
        x -= 1
        while x >= 0 and table[y][x] == 0:
            if index == K:
                a = y
                b = x
                check = True
                break
            table[y][x] = index
            x -= 1
            index += 1
        
        if check:
            break
        y -= 1
        x += 1

    print(b + 1, R - a)