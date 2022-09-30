# 9025 1, 2, 3 더하기

# 4까지 이동한다고 가정했을 때, 1 -> 4, 2 -> 4, 3 -> 4의 경우가 있음
    # 1, 2, 3까지 이동하는 경우에서 각각 3, 2, 1을 더하는 경우
    # 따라서, 4를 만드는 경우의 수는 1, 2, 3을 만드는 경우의 수를 모두 더한 값이 된다
    # 또한, 테스트 케이스 T개에 같은 값을 계속 사용하기 때문에 처음에 초기화 한 값을 재활용
        # 다이나믹 프로그래밍 사용

# 최대 입력 가능 숫자가 11이기 때문에 11까지 모든 경우에 대한 배열을 미리 만들고 입력에 따라 배열에서 값을 찾는 방식
    # 배열의 길이가 11이므로 배열을 사용해도 시간 복잡도에 크게 영향받지 않는다는 판단

T = int(input())

arr = [0, 1, 2, 4] + [0] * 8

for i in range(4, 12):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

for _ in range(T):
    N = int(input())

    print(arr[N])