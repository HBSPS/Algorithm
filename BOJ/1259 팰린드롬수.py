while 1:
    N = input()
    N = list(map(int, str(N)))

    if N[0] == 0:
        break

    a = 0

    for i in range(len(N) // 2):
        if N[i] != N[-i-1]:
            a += 1
    
    if a > 0:
        print("no")
    else:
        print("yes")