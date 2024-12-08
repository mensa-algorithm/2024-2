import sys
input = sys.stdin.readline
N = int(input().strip())
arrs = list(map(int,input().split()))
M = int(input().strip())
result = 0
s, e =  1, max(arrs)
while s <= e:
    mid = (s+e)//2
    total=0
    for arr in arrs:
        if arr > mid:
            total += mid
        else: 
            total += arr
    if total <= M:
        result = mid
        start = mid + 1
    else:
        end = mid-1

print(result)