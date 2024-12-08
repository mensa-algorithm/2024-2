import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([(x,y)])  #시작
    visited[x][y] = 1
    seaList = []

    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M: 
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 0:
                    sea += 1
        if sea > 0:
            seaList.append((x,y,sea))

    for x,y,sea in seaList:  #queue 다 돌고 빙산 줄이기
        graph[x][y] = max(0,graph[x][y]-sea)
    
    return 1

ice = []
year = 0
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            ice.append((i,j))


while ice:
    visited = [[0]*M for _ in range(N)]
    group = 0
    delete = []
    for i,j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i,j)
        if graph[i][j] == 0:
            delete.append((i,j)) #바닷물 되버린 빙산
    if group > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delete)))
    year += 1

if group < 2:
    print(0)