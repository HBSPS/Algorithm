# 2007년

answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())

day = 0

for i in range(1, x):
    day += month[i]

day += y - 1

print(answer[day % 7])