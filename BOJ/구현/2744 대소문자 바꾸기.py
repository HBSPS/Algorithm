# 2744 대소문자 바꾸기

a = input()

for letter in a:
    if letter.isupper():
        print(letter.lower(), end='')
    else:
        print(letter.upper(), end='')