import sys
input = sys.stdin.readline
import math
#랜선구하기
K, N = map(int, input().split())

lan = [int(input().rstrip()) for _ in range(K)]
start = 1
end = max(lan)
#투포인터
while start <= end:
    mid = (start+end)//2
    line = 0
    for li in lan:
        line += li // mid
    
    if line < N:
        end = mid -1
    else:
        start = mid + 1


print(end)