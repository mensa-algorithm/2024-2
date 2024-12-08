import sys

input =  sys.stdin.readline
T  = int(input())
for _ in range(T):
    num = int(input())
    ans = 0
    i = 5
    while i <= num:
        ans += num // i
        i *= 5
    print(ans)
