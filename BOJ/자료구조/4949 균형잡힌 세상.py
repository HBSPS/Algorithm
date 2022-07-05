while 1:
    a = list(map(str, input()))

    if a[0] == ".":
        break

    s = []

    cnt = 0

    for i in a:
        if i == "(" or i == "[":
            s.append(i)

        elif i == ")":
            if s and s[-1] == "(":
                s.pop()
            else:
                cnt += 1
                break
        elif i == "]":
            if s and s[-1] == "[":
                s.pop()
            else:
                cnt += 1
                break


    if len(s) != 0:
        cnt += 1

    if cnt == 0:
        print("yes")
    else:
        print("no")