import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [0] * (N+1)

dp[0] = 1

for i in range(1, N+1):
    if i%2 != 0: #홀수일때 경우의 수 0
        continue
    if i<=2:
        dp[i] = dp[i-2] * 3
    else:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-4+1]*2) # 겹치는 부분 고려

print(dp[-1])