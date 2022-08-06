import sys

n = int(sys.stdin.readline())

student_list = list()
for i in range(n):
    student = input().split()
    student_list.append([student[0], int(student[1])])


# key값 리턴
def setting(data):
    return data[1]


# key값을 기준으로 정렬
student_list = sorted(student_list, key=setting)

for stu in student_list:
    print(stu[0], end=' ')
