# 17413 단어 뒤집기 2

S = list(input())

stack = []
answer = ''

check = False

for letter in S:
    if letter == '>':
        check = False
        answer += '>'
    elif check:
        answer += letter
    elif letter == ' ':
        while stack:
            answer += stack.pop()
        answer += ' '
    elif letter == '<':
        check = True
        while stack:
            answer += stack.pop()
        answer += '<'
    else:
        stack.append(letter)

while stack:
    answer += stack.pop()

print(answer)