import sys #tomato bfs
from collections import deque
input = sys.stdin.readline
  
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

col, row, h = map(int, input().split()) #가로,세로,높이
tomato = [[list(map(int, input().split()))for _ in range(row)] for __ in range(h)]
q = deque([])

for i in range(h):
    for j in range(row):
        for k in range(col):
            if tomato[i][j][k] == 1: #익은 토마토 탐색
                q.append((i,j,k))
                
while q:
    z,x,y = q.popleft()
    for l in range(6):
        nz = z + dz[l]
        nx = x + dx[l]
        ny = y + dy[l]
        if 0<=nx<row and 0<=ny<col and 0<=nz<h:
            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1 # years표시
                q.append((nz,nx,ny))
                
                    
years = 0
for i in range(h):
    for j in range(row):
        for k in range(col):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                years = max(years, tomato[i][j][k])

print(years-1) #처음 1년 길게 나옴 -> -1
exit(0)
  
                


