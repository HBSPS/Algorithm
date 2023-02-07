# 1107 리모컨

# 리모컨의 숫자가 고장났으므로 최대한 가까운 숫자로 이동해야 한다
    # 최대 연산을 하더라도 약 1,000,000개 정도이므로 직접 모든 경우를 확인하는 것도 가능
        # 고장난 숫자를 누르는 경우 break를 걸게 되면 시간 복잡도는 더 줄어든다

N = int(input())
M = int(input())

if M != 0:
    wrong = list(map(str, input().split()))
else:
    wrong = []

answer = abs(100 - N)

for num in range(1000001): # 이동하려는 채널의 최댓값이 500,000이다. 또한, 이동하려는 채널의 최댓값이 500,000이지만 채널은 무한대까지 있기 때문
    tmp = 0

    for i in str(num):
        if i in wrong: # 번호를 누를 수 없는 경우: 해당 채널로 직접 이동할 수 없기 때문에 pass
            tmp = 1

    if tmp == 0:
        answer = min(answer, len(str(num)) + abs(num - N))

print(answer)