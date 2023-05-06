# 5635 생일

N = int(input())

students = []

for _ in range(N):
    name, day, month, year = input().split()

    students.append([name, int(day), int(month), int(year)])

students.sort(key=lambda x: (x[3], x[2], x[1]), reverse=True)

print(students[0][0])
print(students[-1][0])