import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N + M):
    tmp = input()

    tmp = tmp.strip('\n')

    if tmp in dict:
        dict[tmp] += 1
    else:
        dict[tmp] = 1

ans = [key for key, value in dict.items() if value == 2] # value로 key값 찾기

ans.sort()
        
print(len(ans))
for i in ans:
    print(i)