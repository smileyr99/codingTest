array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):  # i+1부터 마지막 인텍스 중에 가장 작은 수 선택
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]  # swap

print(array)
