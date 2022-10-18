# 1541 잃어버린 괄호

# 문자열로 들어오는 수식 -> 문자열 슬라이싱을 통해 숫자와 연산자로 구분

# 최소를 만들어야 한다
    # - 연산자 뒤의 값이 제일 크게 만들면 된다
        # - 연산자가 나오고 뒤의 모든 값들을 더하도록 괄호를 친다고 생각하면 됨

# 조건에 의하면 모든 수는 양수와 덧셈, 뺄셈으로 이루어져 있다
    # 조건에 의해, 첫 숫자는 양수이며, 앞에 어떠한 연산자가 붙지 않는다 -> total을 구하는 과정에서 total의 초기값을 첫 숫자로 설정해도 된다

cal = input()

arr = []

cal = cal.split("-")

for i in cal:
    minus = 0

    tmp = i.split("+")

    for j in tmp:
        minus += int(j)
    arr.append(minus)

total = int(arr[0])

for i in arr[1:]:
    total -= i

print(total)