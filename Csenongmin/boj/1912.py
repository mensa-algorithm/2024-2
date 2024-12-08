import sys
input = sys.stdin.readline

INF = int(-1e9)
n = int(input().strip())

num = list(map(int, input().split()))
dp = [INF] * n
temp = 0
localMax= INF

for i in range(n):
    if i == 0:
        dp[i] = num[i]
        temp = dp[i]
        continue
    
    if num[i] >= 0:
            if num[i-1] < 0: # 전값이 음수이면
                dp[i] = max(dp[i-1]+num[i], num[i]) # 음수값에 양수 더한값과 현재값 비교
                if dp[i] == num[i]: # 현재값으로 설정되면 
                     temp = num[i]
                else: 
                     temp = dp[i]
            else:
                dp[i] = dp[i-1]+num[i]
                temp = dp[i] # 연속된 양수들의 합
    else:
        if num[i-1] < 0: # 전 값이 음수이면
            dp[i] = max(dp[i-1]+num[i], max(num[i], num[i-1])) # 비교 후 적용
            temp = dp[i]
        else:
            dp[i] = dp[i-1]+num[i]  # 마이너스 적용 값
        
        localMax = max(localMax,temp) # 연속된 양수들의 합
        
print(max(dp[-1], localMax))