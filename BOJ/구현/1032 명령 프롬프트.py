# 1032 명령 프롬프트

# 파일 이름의 길이가 모두 같다는 조건이 있으므로 첫번째 문자열을 기준으로 설정
    # 각 문자열의 글자를 탐색하며 일치하는 글자가 없다면 ?로 수정

N = int(input())

arr = list(input())

for _ in range(1, N):
    tmp = list(input())
    for i in range(len(arr)):
        if arr[i] != tmp[i]:
            arr[i] = '?'

for i in arr:
    print(i, end="")