from collections import deque
from collections import defaultdict

import numpy as np

# import numpy as np

recently_experience_attack_list = deque([])
dx_dy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_find_attacker_candidates(arr):
    visited = set()
    max_num = float('inf')
    targets = defaultdict(set)
    def is_valid(x, y):
        return 0 <= x < len(arr) and 0 <= y < len(arr[0]) and (x, y) not in visited and arr[x][y] != 0

    # 시작점 찾기
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0:  # 시작점으로, 부서진 포탑은 피한다.
                starting_point = (i, j)
                print("starting_point:", starting_point)
                if starting_point in visited:
                    continue

                if arr[i][j] <= max_num:
                    max_num = arr[i][j]
                    targets[max_num].add((i, j))

                q = deque([starting_point])  # 시작점 세팅

                while q:  # bfs 시작
                    x, y = q.popleft()
                    for dx, dy in dx_dy:
                        nx, ny = x + dx, y + dy
                        if not is_valid(nx, ny):
                            continue
                        if arr[nx][ny] <= max_num:
                            max_num = arr[nx][ny]
                            targets[max_num].add((nx, ny))
                        visited.add((nx, ny))
                        q.append((nx, ny))

    return list(targets.get(max_num))

def bfs_find_victim_candidates(arr, attacker):
    visited = set()
    min_num = -1
    targets = defaultdict(set)
    def is_valid(x, y):
        return 0 <= x < len(arr) and 0 <= y < len(arr[0]) and (x, y) not in visited and arr[x][y] != 0 and (x, y) != attacker

    # 시작점 찾기
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0:  # 시작점으로, 부서진 포탑은 피한다.
                starting_point = (i, j)
                if starting_point in visited and starting_point == attacker:
                    continue

                if arr[i][j] >= min_num:
                    min_num = arr[i][j]
                    targets[min_num].add((i, j))

                q = deque([starting_point])  # 시작점 세팅

                while q:  # bfs 시작
                    x, y = q.popleft()

                    for dx, dy in dx_dy:
                        nx, ny = x + dx, y + dy

                        if not is_valid(nx, ny):
                            continue

                        if arr[nx][ny] >= min_num:
                            min_num = arr[nx][ny]
                            targets[min_num].add((nx, ny))
                        visited.add((nx, ny))
                        q.append((nx, ny))

    return list(targets.get(min_num))


def set_victim(attacker, arr, turn):
    candidates = bfs_find_victim_candidates(arr, attacker)
    print(f"victim candidates: {candidates}")
    if len(candidates) >= 2 and turn > 0:
        max_idx = float('inf')
        temp = deque([])
        for x, y in candidates:
            # recently_experience에 아예없는게 진도배기

            if (x, y) not in recently_experience_attack_list:
                temp.appendleft((x, y))
            # if (x, y) in recently_experience_attack_list and recently_experience_attack_list.index((x, y)) <= max_idx:
            #     temp.append((x, y))
        candidates = list(temp) if len(temp) > 0 else candidates
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 약한 포탑입니다.
    if len(candidates) >= 2:
        max_num = float('inf')
        temp = defaultdict(set)
        for x, y in candidates:
            if (x + y) <= max_num:
                max_num = x + y
                temp[max_num].add((x, y))
        candidates = list(temp.get(max_num))
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 약한 포탑입니다.
    if len(candidates) >= 2:
        max_num = float('inf')
        temp = defaultdict(set)
        for x, y in candidates:
            if y <= max_num:
                max_num = y
                temp[max_num].add((x, y))
        candidates = list(temp.get(max_num))
    return candidates[0]


def set_attacker(arr, turn):
    # 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정됩니다.
    # 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
    candidates = bfs_find_attacker_candidates(arr)
    # print(f"attacker candidates: {candidates}")
    # 만약 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
    if len(candidates) >= 2 and turn > 0:
        min_idx = 0
        temp = []
        for x, y in candidates:
            if (x, y) in recently_experience_attack_list and recently_experience_attack_list.index((x, y)) >= min_idx:
                temp.append((x, y))
        candidates = temp if len(temp) > 0 else candidates
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑입니다.
    if len(candidates) >= 2:
        min_num = 0
        temp = defaultdict(set)
        for x, y in candidates:
            if (x + y) > min_num:
                min_num = x + y
                temp[min_num].add((x, y))
        candidates = list(temp.get(min_num))
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑입니다.
    if len(candidates) >= 2:
        min_num = 0
        temp = defaultdict(set)
        for x, y in candidates:
            if y > min_num:
                min_num = y
                temp[min_num].add((x, y))
        candidates = list(temp.get(min_num))
    return candidates[0]

def find_laser_route(arr, attacker, victim):
    q = deque([(attacker, [attacker])]) # 공격자를 시작점으로 설정
    visited = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    routes = []
    dx_dy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        """경로에 깨진 포탑(0)이 아니다, 공격자가 아니다,"""
        return arr[x][y] != 0 and (x, y) != attacker and not visited[x][y]

    while q:
        pos, path = q.popleft()
        x, y = pos

        if pos == victim: # 종료 조건
            routes.append(path)
            continue

        for dx, dy in dx_dy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(arr)):
                if nx < 0:
                    nx = len(arr) + nx
                else:
                    nx = len(arr) - nx
            if not (0 <= ny < len(arr[0])):
                if ny < 0:
                    ny = len(arr) + ny
                else:
                    ny = len(arr) - ny
            if not is_valid(nx, ny):
                continue
            visited[nx][ny] = True
            q.append(((nx, ny), path + [(nx, ny)]))

    return routes

def execute_laser_attack(arr, routes, attacker, victim):
    # 최단 경로가 정해졌으면, 공격 대상에는 공격자의 공격력 만큼의 피해를 입히며,
    # 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어듭니다. 또한 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격을 받게 되는데,
    # 이 포탑은 공격자 공격력의 절반 만큼의 공격을 받습니다. (절반이라 함은 공격력을 2로 나눈 몫을 의미합니다.)
    attack_status = arr[attacker[0]][attacker[1]]

    """레이저 경로에 공격력 절반의 공격"""
    for x, y in routes[0][1:-1]:
        arr[x][y] = arr[x][y] - (attack_status // 2)

    """목표물에 공격"""
    arr[victim[0]][victim[1]] = arr[victim[0]][victim[1]] - attack_status

def execute_bomb_attack(arr, attacker, victim):
    total_victim = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    dx_dy = [(1, 0), (0,1), (-1,0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    attack_status = arr[attacker[0]][attacker[1]]

    for dx, dy in dx_dy:
        victim_x, victim_y = victim
        nx, ny = victim_x + dx, victim_y + dy
        if not (0 <= nx < len(arr)):
            if nx < 0:
                nx = len(arr) + nx
            else:
                nx = len(arr) - nx
        if not (0 <= ny < len(arr[0])):
            if ny < 0:
                ny = len(arr) + ny
            else:
                ny = len(arr) - ny
        if arr[nx][ny] != 0:
            total_victim[nx][ny] = True
            arr[nx][ny] = arr[nx][ny] - (attack_status // 2)

    """목표물에 공격"""
    arr[victim[0]][victim[1]] = arr[victim[0]][victim[1]] - attack_status
    total_victim[victim[0]][victim[1]] = True

    # print(total_victim)
    return total_victim


def start_attack(arr, attacker, victim):
    total_victim = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    """레이저 공격 루트를 탐색 -> 최단 거리를 반환"""
    routes = find_laser_route(arr, attacker, victim)
    # print(f"laser routes: {routes}")
    # print(np.array(arr))
    """최단 거리가 존재한다면, 레이저 공격 수행하고 함수 종료"""
    if routes:
        execute_laser_attack(arr, routes, attacker, victim)
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i, j) in routes[0][1:]:
                    total_victim[i][j] = True
        return total_victim

    """만약 최단 거리가 존재하지 않는다면, 포탄 공격 수행하고 함수 종료"""
    total_victim = execute_bomb_attack(arr, attacker, victim)

    return total_victim

def set_recently_experience_attack_list(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0: continue
            recently_experience_attack_list.append((i, j))

def clean_round(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] <= 0:
                arr[i][j] = 0

def manage_potab(arr, attacker, total_victim):
    x, y = attacker
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == x and j == y:
                continue
            if total_victim[i][j]:
                continue
            if arr[i][j] == 0:
                continue
            arr[i][j] += 1


def execute_round(arr, turn):
    """1. 공격자 선정"""
    attacker = set_attacker(arr, turn)
    if attacker in recently_experience_attack_list:
        recently_experience_attack_list.remove(attacker)
    recently_experience_attack_list.append(attacker)

    print(f"attacker: {attacker}")
    """2. 공격자가 공격 대상을 선정"""
    victim = set_victim(attacker, arr, turn)

    # 공격자는 핸디캡이 적용되어 N+M만큼의 공격력이 증가됩니다.
    arr[attacker[0]][attacker[1]] += len(arr) + len(arr[0])
    print(f"victim: {victim}")
    """3. 공격자가 공격 대상 공격(레이저 또는 포탑 공격)"""
    total_victim = start_attack(arr, attacker, victim)
    print("공격 이후")
    print(np.array(arr))
    """4. 부서진 포탑있는지 체크하고 부서진게 있다면 체크"""
    clean_round(arr)
    """5. 공격자가 아니며, 공격 대상자도 아닌 포탑에 대해서 공격력 1씩 증가시킴"""
    manage_potab(arr, attacker, total_victim)


if __name__ == '__main__':
    # 첫 번째 줄에 N, M, K가 공백을 사이에 두고 주어집니다.
    # 두 번째 줄부터 N개의 줄에 걸쳐서 N×M 격자에 대한 정보가 주어집니다. 단, 최초에 부서지지 않은 포탑은 최소 2개 이상 존재합니다.
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    """라운드 진행"""
    for i in range(k):
        print(f"{i+1} round start!")
        execute_round(arr, k)
        print(np.array(arr))

    max_num = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= max_num:
                max_num = arr[i][j]
    print(max_num)
