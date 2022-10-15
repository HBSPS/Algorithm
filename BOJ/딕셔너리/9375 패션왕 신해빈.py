# 9375 패션왕 신해빈

# 옷을 입거나 안입거나 + 순서는 상관 없음 -> 조합
    # 경우의 수를 출력하는 것 (각 조합을 일일이 출력하는 것이 아님) -> 딕셔너리로 옷의 종류만 확인해도 됨

# 전체 조합을 사용하기 때문에 곱 연산을 사용하면 된다
    # 옷을 입지 않는 경우도 포함하기 위해 각 옷의 종류에 1을 더한 후 곱해야 한다
    # 단, 모든 옷을 입지 않은 경우를 제외하기 위해 전체 경우의 수에서 1을 빼주어야 한다

for _ in range(int(input())):
    N = int(input())

    cloth = {}

    for i in range(N):
        a, b = map(str, input().split())

        if b in cloth:
            cloth[b] += 1
        else:
            cloth[b] = 1

    total = 1
    for i in cloth.values():
        total *= (i+1)
    print(total - 1)