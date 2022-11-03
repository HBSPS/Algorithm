# 2407 조합

from math import factorial

N, M = map(int, input().split())

print(factorial(N) // (factorial(M) * factorial(N-M)))