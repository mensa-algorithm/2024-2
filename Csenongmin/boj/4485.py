import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def djikstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n - 1 :
            print(f'Problem {count}: {distance[x][y]}')
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

count = 1
while True:
    n = int(input().strip())

    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]

    djikstra()
    count+=1
    