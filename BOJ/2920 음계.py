l = list(map(int, input().split()))

N = len(l)

T = 0

for i in range(N-1):
    if l[i] + 1 == l[i+1]:
        T = 1
    elif l[i] - 1 == l[i+1]:
        T = 2
    else:
        print("mixed")
        T = 0
        break

if T == 1:
    print("ascending")
elif T == 2:
    print("descending")