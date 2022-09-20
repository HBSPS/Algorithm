from collections import deque

# deque.rotate(x) -> 덱을 x만큼 회전
# deque.index(x) -> 덱에서 x의 index를 반환

# 덱 선언
dq = deque()

N, M = map(int, input().split())

# 사용자의 입력값을 통한 덱 초기화
for i in range(N):
    dq.append(i+1)

# 사용자가 찾고자하는 수 입력
arr = list(map(int, input().split()))

# 덱을 rotate한 횟수
cnt = 0

# 사용자가 찾고자하는 수에 대한 for문
for i in arr:
    # 다 뽑을 때 까지 반복
    while 1:
        # 찾고자 하는 값 i와 덱의 첫 값이 같다면 뽑아내고 반복문 종료
        if dq[0] == i:
            dq.popleft()
            break

        else:
            # 찾고자 하는 요소가 덱의 중간보다 앞에 있다면
            if dq.index(i) < len(dq)/2:
                # 같을 때 까지 왼쪽으로 회전
                while dq[0] != i:
                    dq.rotate(-1)
                    cnt += 1
            # 반대로 덱의 중간보다 뒤에 있다면
            else:
                # 같을 때 까지 오른쪽으로 회전
                while dq[0] != i:
                    dq.rotate(1)
                    cnt += 1

print(cnt)