import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
dp = [0] * 100002
dp[N] = 0
for i in range(K+2):
    if i <= N:
        dp[i] = N - i # -1이동
    
    else:
        if i % 2 == 0: # i가 짝수
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)
            if dp[i-1] > dp[i]+1:
                dp[i-1] = dp[i] + 1
        else:
            dp[i] = dp[i-1]+1
        

print(dp[K])    


  