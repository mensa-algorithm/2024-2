import sys  #dfs, 구현 14500.py 테트로미노
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_ans = 0

def dfs(x, y, n, temp):  #ㅗ모양 제외 나머지 테트로미노
    global max_ans
    if n==4:
        max_ans = max(max_ans, temp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]: 
            visited[nx][ny] = 1
            dfs(nx,ny,n+1,temp+graph[nx][ny])
            visited[nx][ny] = 0

def fk(x,y,temp): #ㅗ모양 4방위 값중 가장 작은 값 제외한 합으로 계산
    global max_ans
    f = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            f.append(graph[nx][ny])
    if len(f)==4:  #한 방향 가장 작은 값 빼기
        max_ans = max(max_ans, sum(f) - min(f) + temp)
    elif len(f)==3: # 3방향 합
        max_ans = max(max_ans, sum(f)+temp)
    else:
        return
        
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        fk(i,j,graph[i][j])
        visited[i][j] = 0

print(max_ans)
