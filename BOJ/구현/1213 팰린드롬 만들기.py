# 1213 팰린드롬 만들기

# 팰린드롬: 앞 또는 뒤로 읽어도 같은 결과

# 사전 순 출력 -> 알파벳 순서로 정렬 후 그리디 알고리즘
    # 홀수 개의 문자가 2개 이상인 경우 팰린드롬을 만들 수 없음

name = list(input())

letters = dict()

for letter in name:
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters[letter] = 1

odd = 0
for count in letters.values():
    if count % 2 != 0:
        odd += 1

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    stack = []
    remain = []
    name.sort()

    index = 0
    while index < len(name) - 1:
        if name[index] == name[index + 1]:
            stack.append(name[index])
            index += 2
        else:
            remain.append(name[index])
            index += 1

    if index == len(name) - 1:
        remain.append(name[index])

    answer = ''
    remain.sort()

    for letter in stack:
        answer += letter

    for letter in remain:
        answer += letter

    while stack:
        answer += stack.pop()

    print(answer)