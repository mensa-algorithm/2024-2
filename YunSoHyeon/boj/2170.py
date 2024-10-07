
import sys

N = int(input())
lines = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
lines.sort()

length = 0
cur_start = lines[0][0]
cur_end = lines[0][1]
for start, end in lines[1:]:
    if start > cur_end:
        length += (cur_end - cur_start)
        cur_start = start
    cur_end = max(cur_end, end)
length += (cur_end - cur_start)

print(length)
