import sys

N = int(sys.stdin.readline().strip())
feel  = list(map(int, sys.stdin.readline().split()))
flower = [0]*N
length = 0
maxLength = 0
k = 0
for i in range(N-1, -1, -1): 
    if feel[i] < 0:
        length += 1
        continue
    
    for j in range(0, length*2):
        if (i-j) > -1:
            flower[i-j] = 1
        maxLength = max(maxLength, length)
        length = 0

ans = 0
for f in flower:
    if f ==1:
        ans+=1
maxIdx = 0
maxCount = 0
length = 0

for i in range(N-1, -1, -1):
    if feel[i] < 0:
        length += 1
        continue
    if length == maxLength:  # maxLength에서 가능한 최대 꽃 구하기
        count = 0
        for j in range(0, length*3):
            if (i-j) > -1 and flower[i-j] == 0:
                count += 1

        if count > maxCount: # maxCount값 구하기
            maxCount = count
            maxIdx = i
    length = 0

print(ans+maxCount) # 2n개수 + 3n 추가개수





