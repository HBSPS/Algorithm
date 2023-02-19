# 9019 DSLR

# D -> N이 두 배 (단, 9,999를 넘는다면 10,000으로 나눈 나머지)
# S -> N-1 (단, N이 0 이라면 9,999)
# L -> 자릿수를 왼쪽으로 회전
# R -> 자릿수를 오른쪽으로 회전
    # L과 R의 주의점
        # 비어있는 자리는 0으로 채워야 한다

# 최소한의 명령으로 A를 B로 바꾸는 방법
    # 최단 경로 -> BFS

# 시간제한 6초?
    # 모든 경우에 대한 실행 -> 시간 초과
        # 방문한 노드를 건너뛰는 과정 필요

from collections import deque
import sys

input = sys.stdin.readline

def D(N):
    N = N * 2

    if N > 9999:
        N = N % 10000

    return N

def S(N):
    if N == 0:
        N = 9999
    else:
        N = N - 1

    return N

def L(N):
    first_number = N // 1000
    other_number = N % 1000

    return other_number * 10 + first_number

def R(N):
    other_number = N // 10
    last_number = N % 10

    return last_number * 1000 + other_number

def main(A, B):
    dq = deque()
    dq.append([A, ''])

    visited = [False for _ in range(10000)]

    visited[A] = True

    while dq:
        N, ans = dq.popleft()

        if N == B:
            print(ans)
            return
        
        next_number = D(N)
        if not visited[next_number]:
            dq.append([next_number, ans + 'D'])
            visited[next_number] = True

        next_number = S(N)
        if not visited[next_number]:
            dq.append([next_number, ans + 'S'])
            visited[next_number] = True

        next_number = L(N)
        if not visited[next_number]:
            dq.append([next_number, ans + 'L'])
            visited[next_number] = True

        next_number = R(N)
        if not visited[next_number]:
            dq.append([next_number, ans + 'R'])
            visited[next_number] = True

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    main(A, B)