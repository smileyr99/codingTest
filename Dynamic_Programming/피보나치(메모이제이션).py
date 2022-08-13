# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100


# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:  # 저장되어 있는 경우 해당 값 리턴
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)  # 배열에 값 저장
    return d[x]


print(fibo(4))
