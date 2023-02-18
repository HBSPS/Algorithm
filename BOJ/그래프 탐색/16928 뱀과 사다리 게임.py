# 16928 뱀과 사다리 게임

# 10 X 10의 보드판
    # 최소로 주사위를 굴리는 횟수
    # 뱀 또는 사다리가 있다
        # 뱀 -> 아래로 내려감
        # 사다리 -> 위로 올라감

# 1번 노드와 100번 노드 사이의 최단 경로를 구해야 한다
    # BFS 사용
        # 1부터 시작하여 각 지점에 방문하는 최단 경로를 저장
        # 어차피 1부터 오름차순만 가능 -> 굳이 2차원 배열?

from collections import deque

N, M = map(int, input().split())

board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

ladder = dict()
snake = dict()

dq = deque()

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

dq.append(1)

def BFS():
    while dq:
        a = dq.popleft()

        if a == 100:
            print(board[100])
            break

        for i in range(1, 7):
            next_move = a + i
            if next_move <= 100 and not visited[next_move]:
                # 이동하는 곳에 사다리가 있는 경우
                if next_move in ladder.keys():
                    next_move = ladder[next_move]
                
                # 이동하는 곳에 뱀이 있는 경우
                if next_move in snake.keys():
                    next_move = snake[next_move]

                # 아무것도 없는 경우
                if not visited[next_move]:
                    visited[next_move] = True
                    board[next_move] = board[a] + 1
                    dq.append(next_move)

BFS()