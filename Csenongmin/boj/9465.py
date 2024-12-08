import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    
    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] = dp[1][0]+s[0][1]
    dp[1][1] = dp[0][0] + s[1][1]

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + s[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + s[1][i]

    print(max(dp[0][-1], dp[1][-1]))
    continue
