import sys

N = int(sys.stdin.readline().rstrip())
N_array = [0] * 1000001

# 가게에 있는 전체 부품번호를 입력받아서 인덱스로 기록
for i in input().split():
    N_array[int(i)] = 1

M = int(sys.stdin.readline().rstrip())
M_array = list(map(int, sys.stdin.readline().split()))

for i in M_array:
    if N_array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
