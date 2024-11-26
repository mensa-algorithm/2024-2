import collections

import numpy as np

#0은 빈칸, 1은 머리사람, 2는 머리사람과 꼬리사람이 아닌 나머지, 3은 꼬리사람, 4는 이동 선
# arr = [[3, 2, 1, 0, 0],
#        [4, 0, 4, 0, 0],
#        [4, 4, 4, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]]

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def shoot_ball(direction, line_num, n):
    """방향에 맞춰서 공을 발사한다."""
    """발사한 공이 만약 0이나, 4가 아닌 다른 숫자에 맞는다면 인덱스 반환"""
    if direction[0]: # 공을 쏘는 방향=좌우 방향
        if direction[0] > 0:
            for i in range(n):
                if arr[line_num][i] != 0 and arr[line_num][i] != 4:
                    return (line_num, i)
        else:
            for i in range(n-1, -1, -1):
                if arr[line_num][i] != 0 and arr[line_num][i] != 4:
                    return (line_num, i)
    elif direction[1]: # 공을 쏘는 방향=상하 방향
        if direction[1] > 0:
            for i in range(n-1, -1, -1):
                if 1 <= arr[i][line_num] <= 3:
                    return (i, line_num)
        else:
            for i in range(n):
                if arr[i][line_num] != 0 and arr[i][line_num] != 4:
                    return (i, line_num)

    return None


def dfs_round_find_line(route, arr, i, j):
    if arr[i][j] == 3:
        route.append((i, j))
        return

    for dx, dy in dxdy:
        path_x = i + dx
        path_y = j + dy
        if 0 <= path_x < len(arr) and 0 <= path_y < len(arr[0]) and (path_x, path_y) not in route:
            if arr[path_x][path_y] == 2:
                route.append((path_x, path_y))
                dfs_round_find_line(route, arr, path_x, path_y)
            if arr[path_x][path_y] == 3:
                dfs_round_find_line(route, arr, path_x, path_y)

def round_move(arr, i, j):
    route = []
    for dx, dy in dxdy:
        xx = i + dx
        yy = j + dy
        if 0 <= xx < len(arr) and 0 <= yy < len(arr[0]):
            if arr[xx][yy] == 4:
                next_head_idx = (xx, yy)
                route.append(next_head_idx)
    route.append((i, j))
    # print(route)
    dfs_round_find_line(route, arr, i, j)
    # [(1, 2), (0, 2), (0, 1), (0, 0)] 이거 처럼 path가 설정됨
    # print(np.array(arr))
    for idx, pos in enumerate(route):
        if idx == 0:
            arr[pos[0]][pos[1]] = 1
        elif idx == len(route) - 1:
            arr[pos[0]][pos[1]] = 4
        else:
            next_pos = route[idx + 1]
            arr[pos[0]][pos[1]] = arr[next_pos[0]][next_pos[1]]

def round_execute(arr):
    """오직 이동하는 함수"""
    head_list = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1: # 머리사람 발견 시
                head_list.append((i, j))
    for head in head_list:
        round_move(arr, head[0], head[1]) # 줄을 찾는다.

def dfs_calculate_score(arr, visited, i, j, depth):
    if arr[i][j] == 1: # 머리사람 발견 시 종료
        print("distance:", depth + 1)
        return (depth + 1) ** 2

    score = 0
    for dx, dy in dxdy:
        path_x = i + dx
        path_y = j + dy
        if 0 <= path_x < len(arr) and 0 <= path_y < len(arr[0]) and (path_x, path_y) not in visited:
            if 1 <= arr[path_x][path_y] <= 3:
                visited.add((path_x, path_y))
                res = dfs_calculate_score(arr, visited, path_x, path_y, depth + 1)
                if res is not None:
                    score = res
                    break

    return score if score > 0 else None

def bfs_find_edges(arr, i, j):
    edge_list = []
    visited = set()
    q = collections.deque([(i, j)])

    while q:
        i, j = q.popleft()

        if (i, j) in visited:
            continue

        visited.add((i, j))

        for dx, dy in dxdy:
            path_x = i + dx
            path_y = j + dy
            if 0 <= path_x < len(arr) and 0 <= path_y < len(arr[0]):
                # print(path_x, path_y)
                if arr[path_x][path_y] == 4 or arr[path_x][path_y] == 0:
                    continue
                if arr[path_x][path_y] == 1 or arr[path_x][path_y] == 3:
                    edge_list.append((path_x, path_y))
                q.append((path_x, path_y))

    return edge_list



def after_ball_hit_execute(arr, hit):
    """점수 계산"""
    i, j = hit
    visited = set()
    score = dfs_calculate_score(arr, visited, i, j, 0)
    # print(f"score: {score}")

    """앞 뒤 바꿔주기"""
    if score is not None:
        edge_list = bfs_find_edges(arr, i, j)
        print(f"edge_list: {edge_list}")
        sx, sy = edge_list[0]
        ex, ey = edge_list[1]
        temp = arr[sx][sy]
        arr[sx][sy] = arr[ex][ey]
        arr[ex][ey] = temp

    return score

if __name__ == '__main__':
    #  격자의 크기 n, 팀의 개수 m, 라운드 수 k가 공백을 사이에 두고 주어집니다.
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total_score = 0

    for r in range(1, k+1):
        print(f"round: {r}")
        """1. 라운드를 진행한다.(머리사람을 따라 라인을 이동시킴)"""
        round_execute(arr)

        """2. 공을 발사하기 전 라운드 수로 공의 진행방향과 진행라인을 계산한다."""
        # 1~n, n+1 ~ 2n , 2n+1 ~ 3n, 3n+1 ~ 4n, 4n+1~5n
        x = r // n
        y = r % n
        direction = dxdy[x % 4 if y != 0 else (x-1)%4]
        line_num = y-1 if x <= 1 else n-y-1
        print(f"{x}n+{y}")
        print(direction, line_num)
        hit = shoot_ball(direction, line_num, n)
        print(f"hit:{hit}")
        """만약 result에 인덱스가 반환된다면, 점수를 추가하고, 머리 꼬리 사람위치를 변경함"""
        if hit:
            result = after_ball_hit_execute(arr, hit)
            total_score += (result if result is not None else 0)
        print(np.array(arr))
        print(total_score)

    # print(f"total_score: {total_score}")
