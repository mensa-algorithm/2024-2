import sys
input = sys.stdin.readline

N=int(input().strip())

phy = [tuple((map(int, input().split()))) for _ in range(N)]
ans = [1]*N
for i in range(N):
    for j in range(N):
        if phy[i][0] < phy[j][0] and phy[i][1] < phy[j][1]:
            ans[i] += 1


for li in ans:
    print(li, end=" ")
