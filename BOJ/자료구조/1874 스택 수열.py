N = int(input())

a = []

tmp = []

for i in range(N):
    a.append(int(input()))

for i in range(N):
    tmp.append(N - i)

stack = ["x"]

i = 0

a_p = []

try:
    while i < N:
        if stack[-1] == a[i]:
            stack.pop()
            a_p.append("-")
            i += 1
        else:
            k = tmp.pop()
            stack.append(k)
            a_p.append("+")

    for j in a_p:
        print(j)
except:
    print("NO")