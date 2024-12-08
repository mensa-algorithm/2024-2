import sys
input = sys.stdin.readline

N = int(input().strip())
pt = sorted(list(map(int, input().split())))
health = []
if N % 2 == 1:
    health.append(pt[-1])
    pt = pt[:-1]

for _ in range((len(pt) // 2) - 1):
    health.append(pt[0] + pt[-1])
    pt = pt[1:-1]

print(max(health))


