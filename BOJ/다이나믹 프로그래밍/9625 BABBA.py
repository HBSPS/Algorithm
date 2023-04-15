# 9625 BABBA

# B -> BA
    # A는 +1, B는 그대로
# A -> B
    # A는 -1, B는 +1

K = int(input())

dpA = [1]
dpB = [0]

for i in range(1, K+1):
    dpB.append(dpA[i-1] + dpB[i-1])
    dpA.append(dpB[i-1])

print(dpA[K], dpB[K])