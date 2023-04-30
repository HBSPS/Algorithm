# 2578 빙고

board = []

for _ in range(5):
    board.append(list(map(int, input().split())))

num_list = []

for _ in range(5):
    tmp = list(map(int, input().split()))

    for i in tmp:
        num_list.append(i)

answer = 0
bingo_count = 0

for num in num_list:
    if bingo_count >= 3:
            print(answer)
            break
    
    answer += 1

    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == num:
                board[i][j] = -1
                x = i
                y = j

    # 가로 확인
    bingo_count += 1
    for i in range(0, 5):
        if board[x][i] != -1:
            bingo_count -= 1
            break

    # 세로 확인
    bingo_count += 1
    for i in range(0, 5):
        if board[i][y] != -1:
            bingo_count -= 1
            break

    # 대각선(\)
    if x == y:
        bingo_count += 1
        for i in range(0, 5):
            if board[i][i] != -1:
                bingo_count -= 1
                break

    # 대각선(/)
    if x + y == 4:
        bingo_count += 1
        for i in range(0, 5):
            if board[4-i][i] != -1:
                bingo_count -= 1
                break