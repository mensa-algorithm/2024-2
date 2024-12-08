import sys
input = sys.stdin.readline
n = int(input().strip())

dp = [1 if i**(0.5)%1==0 else 0 for i in range(n+1)]
ans = 4
for i in range(int(n**0.5), 0, -1):
    if dp[n]: #n이 제곱수
        ans=1
        break
    elif dp[n-i**2]: #n이랑 가까운 제곱수를 뺀 나머지가 제곱수
        ans = 2
        break
    else:  
        k = n-i**2 #나머지값
        for j in range(int(k**0.5),0, -1):
            if dp[k-j**2]: # 그 나머지에서 가까운 제곱수를 뺀 나머지가 제곱수
                ans=3
     
print(ans)


