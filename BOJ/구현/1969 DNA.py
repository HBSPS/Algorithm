# 1969 DNA

# 각 자리에서 가장 많은 문자를 고르면 됨
    # 그리디
# 다른 경우는 별도로 count

# DNA의 문자는 4가지
    # A, T, G, C

N, M = map(int, input().split())

DNA_table = []

answer = ''
count = 0

for _ in range(N):
    DNA_table.append(list(input()))

for i in range(M):
    A, T, G, C = 0, 0, 0, 0
    for DNA in DNA_table:
        if DNA[i] == 'A':
            A += 1
        elif DNA[i] == 'T':
            T += 1
        elif DNA[i] == 'G':
            G += 1
        else:
            C += 1

    if max(A, T, G, C) == A:
        answer += 'A'
        count += (T + G + C)
    elif max(A, T, G, C) == C:
        answer += 'C'
        count += (A + G+ T)
    elif max(A, T, G, C) == G:
        answer += 'G'
        count += (A + C + T)
    else:
        answer += 'T'
        count += (A + C+ G)

print(answer)
print(count)