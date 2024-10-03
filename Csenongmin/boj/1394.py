import sys                 #1394.py 어려웠던 점: 규칙 구현, 시간 초과
input = sys.stdin.readline

word = input().rstrip()
password = input().rstrip()

MOD = 900528
ans =  0
temp = 0
for i in range(len(password)):
    idx = word.index(password[i])+1     #현재 문자 순서 
    if i > 0:                           #전 부분도 계산 필요
        ans = (temp*len(word))%MOD      # MOD 
    ans += idx % MOD
    temp = ans
print(ans%MOD)
        


