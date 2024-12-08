import heapq
import sys
n = int(sys.stdin.readline().rstrip())
heap = []
for i in range(n):
    op = int(sys.stdin.readline().rstrip())
    if op < 0: 
        continue
    elif op == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, op)
