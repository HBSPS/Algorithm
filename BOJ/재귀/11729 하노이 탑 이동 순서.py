def hanoi(N, move, mid, to):
    if N == 1:
        print(move, to)
        
    else:
        hanoi(N-1, move, to, mid)
        print(move, to)
        hanoi(N-1, mid, move, to)

N = int(input())

print(2**N - 1)
hanoi(N, 1, 2, 3)