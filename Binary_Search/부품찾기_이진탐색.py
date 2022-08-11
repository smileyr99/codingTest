import sys

N = int(sys.stdin.readline().rstrip())
N_array = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
M_array = list(map(int, sys.stdin.readline().split()))

# 이진탐색 활용 풀이
def binary_search(target, start, end):
    mid = (start + end) // 2
    if start > end:
        return "no"
    if N_array[mid] == target:
        return "yes"
    elif N_array[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)


for i in M_array:
    print(binary_search(i, 0, len(N_array) - 1), end=" ")
