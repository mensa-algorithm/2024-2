import sys #floyd warshall
input = sys.stdin.readline
INF = int(1e9)

N = int(input().strip())
fw = [list(map(int, input().split())) for _ in range(N)]
dist = [[INF]*N for _ in range(N)
        ]
#for i in range(N):
#   dist[i][i] = 0

for i in range(N):
    for j in range(N):
        if fw[i][j] == 1:
            dist[i][j] = 1



for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:  # if there is edge between i and j, INF -> 1
                dist[i][j] = dist[i][k] + dist[k][j]
                
                

for i in range(N):
    for j in range(N):
        dist[i][j] = 0 if dist[i][j] == INF else  1 
        print(dist[i][j], end=" ")
    print("")