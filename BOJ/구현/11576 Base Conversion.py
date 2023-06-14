# 11576 Base Conversion

A, B = map(int, input().split())

A_num = int(input())

A_digit = list(map(int, input().split()))
A_digit = list(reversed(A_digit))

tmp = 0 # 10진법으로 변환한 수
for i in range(len(A_digit)):
    tmp += (A_digit[i] * pow(A, i))

max_digit = 0
while pow(B, max_digit) < tmp:
    max_digit += 1
max_digit -= 1

answer = []
while max_digit >= 0:
    answer.append(tmp // pow(B, max_digit))
    tmp = tmp % pow(B, max_digit)
    max_digit -= 1

for i in answer:
    print(i, end=' ')