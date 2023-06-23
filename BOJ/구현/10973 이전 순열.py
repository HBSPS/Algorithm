# 10973 이전 순열

""" import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
input_arr = list(map(int, input().split()))

input_text = ''
for i in range(N-1):
    input_text += str(input_arr[i])
    input_text += ' '
input_text += str(input_arr[N-1])

input_arr.sort()

visited = [False for _ in range(N)]
answer_list = []

def get_answer(arr, n):
    if n == N:
        tmp = ''
        for i in range(N-1):
            tmp += str(arr[i])
            tmp += ' '
        tmp += str(arr[N-1])

        answer_list.append(tmp)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(input_arr[i])
            get_answer(arr, n+1)
            arr.pop()
            visited[i] = False

get_answer([], 0)

for i in range(len(answer_list)):
    if answer_list[i] == input_text:
        if i == 0:
            print(-1)
            break
        else:
            print(answer_list[i-1])
            break """

import sys

N = int(input())
input_arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if input_arr[i] < input_arr[i-1]:
        target = i-1
        break

else:
    print(-1)
    sys.exit()

for i in range(N-1, 0, -1):
    if input_arr[i] < input_arr[target]:
        input_arr[i], input_arr[target] = input_arr[target], input_arr[i]
        break

input_arr = input_arr[:target+1] + sorted(input_arr[target+1:], reverse=True)
print(*input_arr)