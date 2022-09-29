# 1620 나는야 포켓몬 마스터 이다솜

# list로 만들어서 입력에 따라 list에서 값을 찾도록 하는 방법 => 시간 초과 (sys 써도 안됨)

''' N, M = map(int, input().split())

arr = [0]

for i in range(N):
    arr.append(input())

for i in range(M):
    tmp = input()

    if tmp.isdigit():
        print(arr[int(tmp) + 1])
    else:
        print(arr.index(tmp)) '''

# 딕셔너리 구조 사용
    # key : value 쌍으로 각각 번호 : 이름 / 이름 : 번호의 두 딕셔너리 생성

# 입력의 개수가 많아 input으로는 시간초과 발생 -> sys.stdin.readline 사용

import sys

N, M = map(int, input().split())

dict1 = {} # 번호 : 이름
dict2 = {} # 이름 : 번호

for i in range(1, N+1):
    tmp = input()

    dict1[i] = tmp
    dict2[tmp] = i

for _ in range(M):
    tmp = sys.stdin.readline().strip()

    if tmp.isdigit():
        print(dict1[int(tmp)])
    else:
        print(dict2[tmp])