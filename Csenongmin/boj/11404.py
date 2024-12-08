import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
m = int(input().strip())

dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):  #자기 자신은 0
    dist[i][i] = 0

for _ in range(m):
    i, j, k = map(int, input().split())
    dist[i][j] = min(dist[i][j],k)  #초기 dist값

for k in range(1,n+1):  #k는 거쳐가는 수
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:  #거쳐서 가는 경우가 더 비용이 적으면
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            dist[i][j] = 0
        print(dist[i][j], end=" ")
    print("")
