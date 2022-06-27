import sys

queue = []

N = int(input())

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

