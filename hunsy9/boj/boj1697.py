from collections import deque
def bfs():
    q = deque()
    q.append(subinX)
    while q:
        xPos = q.popleft()
        if xPos == brotherX:
            print(visited[xPos])
            break
        for i in [xPos-1, xPos+1 , xPos*2]:
            if not visited[i] and 0 <= i <= max_num:
                visited[i] = visited[xPos] + 1
                q.append(i)

subinX, brotherX = map(int, input().split())

max_num = 100000
visited = [0] * (max_num + 1)

bfs()








