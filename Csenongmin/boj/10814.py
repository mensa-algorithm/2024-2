import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
q = []
for i in range(n):
    age, name = input().split()
    heapq.heappush(q, (int(age), i, name))
for i in range(n):
    age, _, name = heapq.heappop(q)
    print(age, end=" ")
    print(name)
