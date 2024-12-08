import sys
import math
n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        continue
    if i % 3 == 0:
        if i % 2 == 0:
            dp[i] = min(dp[i//3],dp[i//2]) + 1
        else: 
            dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif i % 2 == 0 :
        dp[i] = min(dp[i//2],dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1
    
print(dp[n])