import sys

n = int(sys.stdin.readline().rstrip())

dp = [-1] * (n+1)

for i in range(3, n+1):
    if i == 4: continue
    if i % 5 == 0: 
        dp[i]=i//5
    elif i%3 ==0 and i<10:
        dp[i] = i//3
    else:
        if dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
        else:
            if dp[i-3] != -1:
                dp[i] = dp[i-3] + 1

print(dp[n])