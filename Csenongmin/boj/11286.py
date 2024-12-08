import heapq
import sys
n = int(sys.stdin.readline().rstrip())

abs_heap=[]
for i in range(n):
    op = int(sys.stdin.readline().rstrip())
    
    if op < 0:
        heapq.heappush(abs_heap, (-op,op))
    elif op > 0:
        heapq.heappush(abs_heap, (op, op))
    else: 
        if len(abs_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])
        