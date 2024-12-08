import sys
input = sys.stdin.readline


R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


up = -1
down = -1

# 공기 청정기 위치 찾기
for i in range(R):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

def spread():  # 미세먼지 확산
    temp = [[0]*C for _ in range(R)]  #미세먼지 update용
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for x in range(R):
        for y in range(C):
            if graph[x][y] != 0 and graph[x][y] != -1:
               
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        temp[nx][ny] += graph[x][y] // 5
                        count += graph[x][y] // 5
                graph[x][y] -= count

    for i in range(R):
        for j in range(C):
            graph[i][j] += temp[i][j] #복사

def rotate_up():
    dx = [0, -1, 0, 1]  #반시계
    dy = [1, 0, -1, 0]
    before = 0
    direct = 0

    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y==0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

def rotate_down():
    dx = [0, 1, 0, -1]  #시계
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0

    x, y= down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y==0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

# T초 후 미세먼지 양은?
for _ in range(T):
    spread()
    rotate_up()
    rotate_down()
 

answer = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            answer += graph[i][j]
print(answer)