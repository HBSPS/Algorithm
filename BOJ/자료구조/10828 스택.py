import sys

stack = []

N = int(input())

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(cmd[1])