import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int,sys.stdin.readline().split())
maize = [list(map(int, ' '.join(sys.stdin.readline().split()))) for _ in range(N)]
queue = deque([(0,0)]) # 시작

#BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if maize[next_x][next_y] == 1:
                queue.append((next_x,next_y))
                maize[next_x][next_y] = maize[x][y] + 1 #이동횟수로 표현
        
print(maize[N-1][M-1])