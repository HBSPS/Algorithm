# 5800 성적 통계

for i in range(int(input())):
    print('Class', (i+1))

    score = list(map(int, input().split()))
    del score[0]

    score.sort()

    max_gap = 0
    for a in range(1, len(score)):
        if score[a] - score[a-1] > max_gap:
            max_gap = score[a] - score[a-1]

    print('Max', str(max(score))+',' ,'Min', str(min(score))+',', 'Largest gap', max_gap)