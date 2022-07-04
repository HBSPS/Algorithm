from collections import deque

D = deque()

N = int(input())

for i in range(N):
    I = input().split()

    if I == "push_front":
        D.appendleft(I[1])
    elif I == "push_back":
        D.append(I[1])
    elif I == "pop_front":
        if len(D) == 0:
            print(-1)
        else:
            D.popleft()
    elif I == "pop_back":
        if len(D) == 0:
            print(-1)
        else:
            D.pop()
    elif I == "size":
        print(len(D))
    elif I == "empty":
        if len(D) == 0:
            print(1)
        else:
            print(0)
    elif I == "front":
        if len(D) == 0:
            print(-1)
        else:
            print(D[0])
    elif I == "back":
        if len(D) == 0:
            print(-1)
        else:
            print(D[-1])