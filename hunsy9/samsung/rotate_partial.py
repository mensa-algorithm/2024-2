# 7X7 배열
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sy, sx = 2, 2
length = 3


# 배열의 특정 부분(정사각형)을 회전시킴
def rotate_90(sy, sx, length):
    global arr, new_arr
    # 정사각형을 시계방향으로 90도 회전
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            # 1단계 : (0,0)으로 옮겨주는 변환을 진행함
            oy, ox = y - sy, x - sx
            # 2단계 : 90도 회전했을때의 좌표를 구함
            ry, rx = ox, length - oy - 1
            # 3단계 : 다시 (sy,sx)를 더해줌
            new_arr[sy + ry][sx + rx] = arr[y][x]

    # new_arr 값을 현재 board에 옮겨줌
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            arr[y][x] = new_arr[y][x]
            print(arr[y][x])

rotate_90(sy, sx, length)

for i in range(len(arr)):
    print(arr[i])