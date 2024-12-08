#14916
import sys

n = int(sys.stdin.readline().rstrip()) # 총 거스름돈
dp = [-1] * (n+1)  # 거슬러줄 수 없을때에는 -1출력
for i in range(2, n+1):
    if i==3: continue
    if i % 5 == 0:  # 5의 배수는 5원으로 주는게 항상 최소
        dp[i] = i // 5
    elif i % 2==0 and i <= 8:  # 8원 이하 2의 배수는 2원으로 주는게 항상 최소
        dp[i] = i//2
    else:
        dp[i] = dp[i-5] + dp[5] # 금액이 큰 5원을 기준으로 해야 최소.

print(dp[n])  # 금액이 n일 떄의 최소 동전 개수.

