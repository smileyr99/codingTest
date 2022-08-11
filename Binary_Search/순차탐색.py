def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1  # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)


array = ["Hanul", "Jonggu", "Dongbin", "Taeil", "Sangwork"]
n = len(array)
target = "Dongbin"
print(sequential_search(n, target, array))
