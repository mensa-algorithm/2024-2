import sys
input= sys.stdin.readline

T, W = map(int, input().split())

li = [int(input().strip()) for _ in range(T)]

dp = [[0 for _ in range(T+1)] for _ in range(W+1)]
for k in range(W+1):  # K는 자두가 움직인 횟수
    for i in range(1,T+1):
        if k==0:
            point = 1 if li[i-1] == 1 else 0
            dp[k][i] = dp[k][i-1] + point
        elif k%2==0: #k가 짝수 -> 최종 위치는 1.
            point = 1 if li[i-1] == 1 else 0 
        else:  #k가 홀수 -> 최종 위치는 2.
            point = 1 if li[i-1] == 2 else 0
        dp[k][i] = max(dp[k][i-1]+point, dp[k-1][i-1]+point)
ans = []
for i in range(W+1):
    ans.append(dp[i][-1])
print(max(ans))
