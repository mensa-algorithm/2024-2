from collections import deque

delta = [[1,0], [0,1], [-1,0],[0,-1]]
count = 0
def bfs(graph, s_node , visited, m, n):
    queue = deque([s_node])
    visited[s_node[0]][s_node[1]] = True
    while queue:
        node = queue.popleft()
        for dxdy in delta:
            newX = node[1] + dxdy[1]
            newY = node[0] + dxdy[0]
            if (newX >= 0 and newX < m) and (newY >= 0 and newY < n):
                if not visited[newY][newX] and graph[newY][newX] != 0:
                    queue.append([newY,newX])
                    visited[newY][newX] = True
def findAll():
    m, n, b = map(int, input().split())
    count = 0
    visited = [[False] * m for i in range(n)]
    graph = [[0] * m for i in range(n)]
    for i in range(b):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(m):
        for j in range(n):
            if graph[j][i] != 0 and not visited[j][i]:
                count+=1
                bfs(graph, [j,i], visited, m, n)
    print(count)

n=int(input())
for i in range(n):
    findAll()








