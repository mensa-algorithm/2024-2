import sys
from collections import deque

def bfs(x, y, matrix):
    q = deque([(x, y)])
    distance = [[987654321] * len(matrix[0]) for _ in range(len(matrix))]
    distance[x][y] = 0
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
                continue
            if matrix[nx][ny] == 'L' and not visited[nx][ny]:
                distance[nx][ny] = distance[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
    valid_distance = [num for row in distance for num in row if num != 987654321]
    return max(valid_distance)

def main():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    matrix = [input().strip() for _ in range(a)]
    max_cnt = 0 
    for i in range(a):
        for j in range(b):
            if matrix[i][j] == 'L':
                cnt = bfs(i,j,matrix)
                if cnt > max_cnt:
                    max_cnt = cnt
    print(max_cnt)

if __name__ == "__main__":
    main()