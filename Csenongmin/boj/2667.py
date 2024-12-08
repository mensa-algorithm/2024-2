import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]


num = []

N = int(sys.stdin.readline().strip())
m = [list(map(int, ' '.join(sys.stdin.readline().split()))) for _ in range(N)]

def dfs(x, y):
    if 0 <= x < N and 0 <= y < N:
        if m[x][y] == 1:
            global count
            count += 1
            m[x][y] = 0    
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                dfs(next_x, next_y)  #recursive
            return True
        else:
            return False
    else:
        return False
    
count = 0
result = 0

for x in range(N):
    for y in range(N):
        if dfs(x,y) == True:
            num.append(count)
            result += 1
            count = 0
        else:
            continue


print(result)
num.sort()
for i in range(len(num)):
    print(num[i])
