# 문제 링크 : https://www.acmicpc.net/problem/1520
# 문제 해설 : https://internetrecord.tistory.com/31

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n,m = map(int , input().split())
maps = [list(map(int , input().split())) for _ in range(n)]  
dx=[-1,0,1,0]
dy=[0,1,0,-1]
dp = [ [-1]*m for _ in range(n)]

def in_range(row,col) :
    if row>=0 and row<n and col>=0 and col<m :
        return True
    return False
    
def dfs(row, col) :
    # 값이 있다면 return
    if dp[row][col] != -1 :
        return dp[row][col]
    
    if row == n-1 and col == m-1 :
        return 1

    dp[row][col] = 0
    
    for i in range(4) :
        next_row = row + dx[i]
        next_col = col + dy[i]
        if in_range(next_row,next_col) :    
            if maps[row][col] > maps[next_row][next_col] :
                dp[row][col] += dfs(next_row,next_col)
    return dp[row][col]

dfs(0,0)
print(dp[0][0])