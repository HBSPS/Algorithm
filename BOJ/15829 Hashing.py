L = int(input())

a = list(map(str, input()))
b = []
total = 0

for i in a:
    b.append(ord(i)-96)

for i in range(len(b)):
    total += b[i] * (31 ** i)

print(total % 1234567891)