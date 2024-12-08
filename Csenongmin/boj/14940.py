import sys #bfs
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]


graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:  # goal location
            q.append((i,j))
            visited[i][j] = 1 # check visited.
            graph[i][j] = 0   # set cost to 0
            break

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] > 0:  # cannot visit because of wall
            graph[i][j] = -1
        print(graph[i][j], end=" ")
    print("")

