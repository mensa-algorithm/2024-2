import collections

global frac_idx
frac_idx = 0

def partial_rotate(arr, crit, angle):
    copied_arr = [row[:] for row in arr]
    x, y = crit
    arr_part = []
    for i in range(x - 1, x + 2):
        arr_part.append(copied_arr[i][y - 1:y + 2])
    r_arr = None
    if angle == 90:
        r_arr = list(map(list, zip(*arr_part[::-1])))
    elif angle == 180:
        r_arr = [row[::-1] for row in arr_part[::-1]]
    elif angle == 270:
        r_arr = list(map(list, zip(*arr_part)))[::-1]

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            copied_arr[i][j] = r_arr[i - (x - 1)][j - (y - 1)]
    return copied_arr


def get_connected_components_number(arr):
    visited = [[False for _ in range(5)] for _ in range(5)]
    dx_dy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    routes = []

    def bfs(x, y):
        value = arr[x][y]
        q = collections.deque([(x, y)])
        path = [(x, y)]

        while q:
            x, y = q.popleft()
            visited[x][y] = True

            for dx, dy in dx_dy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and arr[nx][ny] == value:
                    q.append((nx, ny))
                    path.append((nx, ny))
                    visited[nx][ny] = True

        return path if len(path) >= 3 else None

    for i in range(5):
        for j in range(5):
            founded_path = bfs(i, j)
            if founded_path:
                routes.append(founded_path)
    return routes


def make_crit_angle_dict_key(crit, angle, value):
    x, y = crit
    return f"{x}:{y}:{angle}:{value}"


def make_dict(arr, crit, angle, crit_angle_value_arr_dict, crit_angle_value_routes_dict):
    rot_arr = partial_rotate(arr, crit, angle)
    routes = get_connected_components_number(rot_arr)
    value = 0
    if routes:
        for route in routes:
            value += len(route)
    dict_key = make_crit_angle_dict_key(crit, angle, value)
    crit_angle_value_arr_dict[dict_key] = rot_arr
    crit_angle_value_routes_dict[dict_key] = routes


def find_rotated_arr_candidates(arr):
    crit_angle_value_arr_dict = {}
    crit_angle_value_routes_dict = {}

    # 회전기준좌표 : 회전각도: 영역개수 | 배열
    # 딕셔너리 제작
    for i in range(1, 4):
        for j in range(1, 4):
            crit = (i, j)  # 회전 기준점
            angles = [90, 180, 270]
            for angle in angles:
                make_dict(arr, crit, angle, crit_angle_value_arr_dict, crit_angle_value_routes_dict)

    candidate_keys = list(crit_angle_value_arr_dict.keys())
    candidate_keys.sort(
        key=lambda x: (-int(x.split(":")[3]), int(x.split(":")[2]), int(x.split(":")[1]), int(x.split(":")[0])))

    key = candidate_keys[0]
    return {
        "key": candidate_keys[0],
        "rotated_arr": crit_angle_value_arr_dict[key],
        "find_routes": crit_angle_value_routes_dict[key]
    }


def retrieve_item(routes, rotated_arr, fractions):
    total_value = 0

    items = routes
    global frac_idx

    while True:
        """언제 종료할까? items가 다떨어지면"""
        if len(items) == 0 or not items:
            break

        """얻을 유적들을 열이 작은 순으로, 행이 큰 순으로 정렬"""
        target = []
        for r in items:
            for i in r:
                target.append(i)
        target.sort(key=lambda x: (x[1], -x[0]))

        """fractions들로부터 target을 뺑뺑이 돌면서, rotated_arr의 값을 변경"""
        for i in range(len(target)):
            item_target_x, item_target_y = target[i]
            rotated_arr[item_target_x][item_target_y] = fractions[frac_idx]
            frac_idx += 1

        """얻은 아이템의 갯수를 total_value에 더해줌"""
        # print(len(target))
        total_value += len(target)
        # print("연쇄획득")
        # print(np.array(rotated_arr))
        """변경 완료되었다면, 다시한번 연결요소가 없는지 검사하고 있다면, 타겟 아이템을 또 만들어준다."""
        items = get_connected_components_number(rotated_arr)
        # print(items)

    return {
        "total_value": total_value,
        "grid": rotated_arr
    }


def execute_round(grid, fractions):
    """탐색 후보 선정 후 부분 회전 완료된 grid 반환"""
    # print("라운드 시작 유적")
    # print(np.array(grid))
    result = find_rotated_arr_candidates(grid)
    rotated_arr = result.get("rotated_arr")
    # print("돌린 유적")
    # print(result.get("key"))
    # print(np.array(rotated_arr))
    routes = result.get("find_routes")
    if not routes:
        return

    """유적 획득 과정"""
    result = retrieve_item(routes, rotated_arr, fractions)
    print(result.get("total_value"), end=" ")
    # print("라운드 획득 유적 갯수: ", result.get("total_value"))
    return result.get("grid")


if __name__ == '__main__':
    """입력"""
    # 첫 번째 줄에 탐사의 반복 횟수 K와 벽면에 적힌 유물 조각의 개수 M이 공백을 사이에 두고 주어집니다.
    k, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(5)]
    fractions = list(map(int, input().split()))
    for i in range(k):
        grid = execute_round(grid, fractions)
        if grid is None:
            break