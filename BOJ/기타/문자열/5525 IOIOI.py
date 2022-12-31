# 5525 IOIOI
# 문자열

# 문자열 슬라이싱을 통해 Pn과 비교하며 count 증가
'''
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

P = 'I' + 'OI' * N
window = 2 * N + 1
count = 0

for i in range(0, M - window + 1):
    if S[i] == 'O':
        continue
    if S[i:i+window] == P:
        count += 1

print(count)
'''
# 위의 방법을 사용하면 N과 M이 커지면서 시간초과 발생

# arr[a:b]의 경우 시간 복잡도가 O(b-a)
    # S의 전체 탐색은 필수이므로 시간 복잡도를 줄이기 위해서는 슬라이싱에서 최소화 해야 함 -> N이 커지게 되면 슬라이싱의 범위가 늘어나기 때문
    # 따라서, 위의 방식대로 슬라이싱 하는 대신 슬라이싱 범위를 2로 줄임
        # I 뒤에는 OI가 있어야 함
            # I뒤에 연속된 OI의 갯수를 측정 (ex. IOIOI에 있는 연속된 OI의 갯수는 2)
            # 해당 갯수를 별도의 배열에 저장해두고 (OI의 갯수 - N + 1)를 통해 Pn이 몇 번 포함되는지 계산 (ex. IOIOIOI에서 OI의 갯수는 3, N이 2일 때 IOIOIOI에 IOIOI는 2번 포함)

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

index = 0
answer = []
count = 0

while index < M :
    if S[index] == 'O':
        index += 1
    else:
        if S[index + 1 : index + 3] == 'OI':
            count += 1
            index += 2
        else:
            answer.append(count)
            index += 1
            count = 0

result = 0  
for i in answer:
    tmp = i - N + 1
    if tmp >= 0:
        result += tmp

print(result)