# 25206 너의 평점은

lecture = []
count = 0  # 성적에 반영되는 과목의 수
total_score = 0

for i in range(20):
    lecture.append(list(input().split()))

for item in lecture:
    if item[2] == 'P':
        continue    
    
    count += eval(item[1])

    if item[2] == 'A+':
        total_score += (4.5 * eval(item[1]))
    elif item[2] == 'A0':
        total_score += (4.0 * eval(item[1]))
    elif item[2] == 'B+':
        total_score += (3.5 * eval(item[1]))
    elif item[2] == 'B0':
        total_score += (3.0 * eval(item[1]))
    elif item[2] == 'C+':
        total_score += (2.5 * eval(item[1]))
    elif item[2] == 'C0':
        total_score += (2.0 * eval(item[1]))
    elif item[2] == 'D+':
        total_score += (1.5 * eval(item[1]))
    elif item[2] == 'D0':
        total_score += (1.0 * eval(item[1]))
    else:
        total_score += 0

print(total_score / count)