import sys  #greedy, sort
import heapq
input = sys.stdin.readline
schd = []
n = int(input().strip())
for i in range(n):
    x,y = map(int, input().split())
    heapq.heappush(schd, (y,x)) # 가장먼저 끝나는 시간, 시작 시간 순으로 정렬

count = 0
e, s = 0, 0
for _ in range(n):
    e2, s2 = heapq.heappop(schd)
    
    if s2 < e:    
        continue
    elif s2 >= e:
        count += 1
        e, s = e2, s2


print(count)