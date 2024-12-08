import sys  #bfs
from collections import deque
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n, m = map(int, input().split())
campus = [input().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque([])
count = 0

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I": #Doyeon's location
            q.append((i,j))
            visited[i][j] = 1
            break

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if campus[nx][ny] !="X" and not visited[nx][ny]:
                if campus[nx][ny] == "P": # meets friend
                    count += 1
                q.append((nx,ny))
                visited[nx][ny] = 1

print(count if count > 0 else "TT")