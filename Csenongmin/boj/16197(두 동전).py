import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
coin = []

for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(M):
        if graph[i][j] == "o":
            coin.append((i, j))

q = deque()  #첫번째 위치
q.append((coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0))

def bfs():
    while q:
        x1,y1,x2,y2 , count = q.popleft()  # 두 동전 위치 가져오기
        if count >= 10:
            return -1
    
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if graph[nx1][ny1] == '#': # c1 벽
                    nx1, ny1 = x1, y1
                if graph[nx2][ny2] == '#':  # c2 벽
                    nx2, ny2 = x2, y2
                q.append((nx1,ny1,nx2,ny2,count+1))

            elif 0 <= nx1 < N and 0 <= ny1 < M:
                return count+1
            elif 0 <= nx2 < N and 0 <= ny2 < M:
                return count+1
    return -1

print(bfs()) 