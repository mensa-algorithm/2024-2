import sys  #bfs
from collections import deque
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            q.append((i,j))  # initial tomato's location

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if box[nx][ny]==0:
                box[nx][ny] = box[x][y]+1  # total days. 
                q.append((nx,ny))          # in bfs, optimal minimum days.

days = 0
for tomato in box:
    if 0 in tomato:
        print(-1)
        exit(0)
    days = max(days, max(tomato))
print(days-1)