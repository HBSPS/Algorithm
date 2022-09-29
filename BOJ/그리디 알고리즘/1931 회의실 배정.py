# 1931 회의실 배정

# 주어진 회의 시간을 적절히 배치해서 최대 회의 배정 -> 그리디 알고리즘
# 가장 시간이 적게 걸리는 회의부터 시작하여 끝나는 시간과 제일 가까우면서 가장 시간이 적게 걸리는 회의 배정

# 최소를 찾기 위해 배열에 값을 저장하고 sort -> 2차원 배열에 sort를 하게 되면 각 요소의 0번 index에 대해 오름차순 정렬을 하고, 같은 값이라면 1번 index를 오름차순 정렬
    # 또는, sort에 lambda를 사용하여 특정 index에 대해 오름차순/내림차순 정렬 가능
        # .sort(key=lambda x:(x[1], x[0]))의 형식으로 사용 -> 2차원 배열에서 1번 index에 대해 오름차순 정렬 후, 1번 index가 같다면 0번 index에 대해 오름차순 정렬
        # 내림차순 정렬을 하고 싶다면 -를 붙이면 됨 -> sort(key=lambda x:(-x[1], -x[0])) : 위와 같은 조건이지만 내림차순 정렬

N = int(input())

arr = []

for i in range(N):
    start, end = map(int, input().split())

    arr.append([start, end])

arr.sort(key=lambda x:(x[1], x[0])) # 2차원 배열에서 1번 index에 대해 오름차순 정렬 후, 1번 index가 같다면 0번 index에 대해 오름차순 정렬

cnt = 0
end = 0

for s, e in arr:
    if s >= end:
        cnt += 1
        end = e


print(cnt)