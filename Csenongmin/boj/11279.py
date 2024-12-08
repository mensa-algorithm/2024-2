import heapq
import sys
n = int(sys.stdin.readline().rstrip())

max_heap =[]
for i in range(n):
    op = int(sys.stdin.readline().rstrip())
    if op < 0:
        continue
    elif op > 0:
        heapq.heappush(max_heap, (-op, op))
    else :
        if len(max_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])