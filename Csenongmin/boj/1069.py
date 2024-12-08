import sys
import math

input = sys.stdin.readline

X, Y, D, T = map(int, input().split())

distance = math.sqrt(X**2 + Y**2)
ans = 0
if D > distance:
    ans = min(distance, T + D-distance, 2*T) # 걷기, 점프+걷기, 점프 중 최단시간

elif D < distance:
    ans = min(distance, (distance//D)*T + (distance%D), (distance//D + 1) * T) # 걷기 ,점프+걷기, 점프 중 최단시간

else: # D == distance
    ans = min(distance, T)

print(ans)