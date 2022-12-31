# 2407 조합
# 수학 / 조합론 / 임의 정밀도 / 큰 수 연산

from math import factorial

N, M = map(int, input().split())

print(factorial(N) // (factorial(M) * factorial(N-M)))