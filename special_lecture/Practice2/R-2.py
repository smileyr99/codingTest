import sys

n = int(sys.stdin.readline())
Alst = list(map(int, sys.stdin.readline().split()))
Blst = list()
idx = Alst.copy()
tmp = list()
cnt = 0

while(True):
    k = Alst[cnt]
    Alst.remove(Alst[cnt])
    for j in Alst:
        if j > k:
            tmp.append(idx.index(j))
    Blst.append(min(tmp))
    tmp = []
    if len(Alst) == 1:
        break

print(*Blst)






