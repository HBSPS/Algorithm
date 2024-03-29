# 1057 토너먼트

# 두 명의 참가자는 항상 이긴다는 가정하에 몇 라운드에서 서로 만나게 되는지 구하는 문제
    # 토너먼트 형식 + 항상 이긴다는 조건에 의해 둘이 경기하지 않는 경우는 존재하지 않는다
    # 토너먼트의 특성상 자신의 16명 중 8번인 선수가 이긴다면 8강에서는 4번이 된다
        # 마찬가지로, 16명 중 9번인 선수가 이긴다면 8강에서는 5번이 된다
    # 따라서, 선수의 다음 라운드 번호는 자신의 현재 번호 / 2를 반올림 한 값이다
        # (또는, 자신의 현재 번호 - 자신의 현재 번호를 2로 나눈 몫)
    # 두 선수의 번호가 같아지기 직전 두 사람이 경기를 하게 된다

N, a, b = map(int, input().split())

count = 0

while a != b:
    a = a - a // 2
    b = b - b // 2
    count += 1

print(count)