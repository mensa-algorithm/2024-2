
import sys
input = sys.stdin.readline

lecture, blu_ray = map(int, input().split())
time = list(map(int, input().split()))

start = max(time)
end = sum(time)

while start <= end:
    blu_ray_counting = 0
    cur_time = 0    # 블루레이의 현재 길이를 나타내고, mid보다 커질 때마다 새로운 블루레이가 필요함을 나타내어 count를 증가시키는데 활용
    mid = (start + end) // 2

    for length in time:
        if cur_time + length > mid:
            cur_time = 0
            blu_ray_counting += 1
        cur_time += length

    if cur_time != 0:
        blu_ray_counting += 1

    if blu_ray_counting <= blu_ray:
        end = mid - 1
    else:
        start = mid + 1

print(start)
