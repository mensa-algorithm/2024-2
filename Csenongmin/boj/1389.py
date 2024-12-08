import sys #floyd warshall
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
kebin = []               
for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        temp += graph[i][j]
    kebin.append(temp)

print(kebin.index(min(kebin))+1)