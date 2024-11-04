from collections import deque
import sys

n = int(sys.stdin.readline())
visited = [[False] * n for i in range(n)]
graph = [[i for i in input()] for i in range(n)]

pushedList = []

x_y = [[1,0],[0,1],[-1,0], [0,-1]]

def bfs(startX, startY , visited):
    snode = [startX,startY]
    queue = deque([snode])
    visited[startX][startY] = True
    count = 1
    while queue:
        node = queue.popleft()
        for dxdy in x_y:
            newX = node[0] + dxdy[0]
            newY = node[1] + dxdy[1]
            if (newX >= 0 and newX < n) and (newY >= 0 and newY < n):
                if not visited[newX][newY] and graph[newX][newY] != '0':
                    newNode = [newX, newY]
                    visited[newX][newY] = True
                    queue.append(newNode)
                    count+=1
    pushedList.append(count)

for k in range(n):
    for l in range(n):
        if graph[k][l] == '1' and not visited[k][l]:
            bfs(k, l, visited)
pushedList.sort()
print(len(pushedList))
for i in pushedList:
    print(i)


