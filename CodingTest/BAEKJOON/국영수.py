import sys

N = int(sys.stdin.readline())
Student = [ sys.stdin.readline().split() for i in range(N) ]

for student in sorted(Student, key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(student[0])
