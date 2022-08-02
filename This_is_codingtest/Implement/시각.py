import sys

h = int(sys.stdin.readline())
cnt = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # s : 매 시각
            s = str(i) + str(j) + str(k)
            # 매 시각에 '3'이 포함되어 있을 경우
            if '3' in s:
                cnt += 1

print(cnt)
