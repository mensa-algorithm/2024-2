import sys 

n,m = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
#dp=[[-1 for _ in range(n)] for _ in range(n)]
 
dp=[0 for _ in range(m)] # 나머지의 수

p=0
for i in range(n):
    p+=seq[i]
    dp[p%m]+=1

ans=dp[0]
for i in range(m) :
    ans += dp[i] * (dp[i]-1) // 2

print(ans)
