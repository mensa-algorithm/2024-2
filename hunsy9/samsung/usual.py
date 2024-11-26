import numpy as np

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(np.array(arr))
print()

print(np.array(arr[::-1]))
# zip

# 시계 방향 90 (= 반시계 방향 270)
# arr[::-1] -> 역순 출력
arr_90 = list(map(list, zip(*arr[::-1])))
print(np.array(arr_90))
print()

# 시계 방향 180 (= 반시계 방향 180)
arr_180 = [a[::-1] for a in arr[::-1]]
print(np.array(arr_180))
print()

# 시계 방향 270 (= 반시계 방향 90)
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
print(np.array(arr_270))
print()

print(list(range(7, 0, -1)))