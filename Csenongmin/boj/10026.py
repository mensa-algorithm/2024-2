import sys  #dfs, bfs , sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀함수 횟수 한계 증가 dfs recursive를 쓸 때에는 백준에선 이거 써야한다..
N = int(input().strip())
grid = [input().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y,color):
    if 0<=x<N and 0<= y <N:
        if grid[x][y]==color and not visited[x][y]:
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny,color)
            return True
        else:
            return False
    else:   
        return False
    
# for normal person.
count = 0
count_rg = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if dfs(i,j,grid[i][j]):
                count +=1

## for red-green color blindness
grid = [["R" if color=="R" or color=="G" else "B" for color in colors] for colors in grid]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if dfs(i,j,grid[i][j]):
                count_rg += 1
        
print(count, count_rg)