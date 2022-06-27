N = list(map(int, input().split()))

T = 0

for i in range(5):
    T += N[i] ** 2

print(T%10)