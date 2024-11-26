import collections

# 왕의 명령 방향. 차례대로 상우하좌
command_direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Knight:
    def __init__(self, list):
        idx, x, y, h, w, k = list
        self.idx = idx
        self.location = []
        for i in range(x-1, x - 1 + h):
            for j in range(y-1, y - 1 + w):
                self.location.append((i, j))
        self.health = k
        self.initial_health = k
        self.disabled = False
    def __repr__(self):
        return f"[Knight {self.idx}: {self.location}, health: {self.health}, disabled: {self.disabled}]"

    def move(self, direction):
        dx, dy = command_direction[direction]
        temp_location = []
        for x, y in self.location:
            nx, ny = x + dx, y + dy
            temp_location.append((nx, ny))
        self.location = temp_location

    def get_damage(self):
        damage_count = 0
        for x, y in self.location:
            if landform[x][y] == 1: # 함정이라면
                damage_count += 1
        self.health -= damage_count
        if self.health <= 0:
            self.location = [] # 체스판에서 사라짐
            self.disabled = True # 불능상태 처리


def get_movable_knights_candidate(command, knights_map, knights_grid, landform):
    knight_idx, direction = command
    dx, dy = command_direction[direction]

    candidates = set()

    searching_knights = collections.deque([])
    searching_knights.append(knight_idx)

    while searching_knights: # 연쇄 반응에서 벽이 검출된다면 정지
        curr_knight = knights_map[searching_knights.popleft()]
        future_locations = [(x+dx, y+dy) for x, y in curr_knight.location[:]]

        """미래 방향에 기사 또는 지형물(벽)이 있는지 검사"""
        for x, y in future_locations:
            if not (0 <= x < len(landform) and 0 <= y < len(landform)) or landform[x][y] == 2: # landform 밖의 벽이라면
                return []

            if knights_grid[x][y] == curr_knight.idx: # 자기 자신이면 무시
                continue

            if knights_grid[x][y] != 0: # 자기자신이 아닌 기사랑 부딫혔을 때
                searching_knights.append(knights_grid[x][y])

        """탐색을 마친 기사는 후보자에 넣어줌"""
        candidates.add(curr_knight.idx)
    return candidates

def command_from_king(command, knights_map, knights_grid, landform):
    knight_idx, direction = command

    """만약 명령이 사라진 기사에 대한 명령이라면 무효처리"""
    if knights_map[knight_idx].disabled:
        return

    """get_movable_knights_candidate를 통해 움직일 수 있는 기사들의 리스트를 구해보자."""
    knights_candidate = get_movable_knights_candidate(command, knights_map, knights_grid, landform)

    """리스트 순회하며, move 메서드 호출 -> 자동으로 기사들의 위치 업데이트"""
    for knight in knights_candidate:
        knights_map.get(knight).move(direction)

    """이동명령을 받은 기사를 제외한 나머지 기사들에 대하여 현재 위치에 각각 함정이 몇 개씩인지 세고, 체력 낮추기"""
    for knight in knights_candidate:
        if knight != knight_idx:
            knights_map.get(knight).get_damage()

    """knight_grid 업데이트"""
    # knights_grid = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(len(knights_grid)):
        for j in range(len(knights_grid[0])):
            knights_grid[i][j] = 0
    for k in list(knights_map.values()):
        for i, j in k.location:
            knights_grid[i][j] = k.idx


if __name__ == '__main__':
    L, N, Q = map(int, input().split()) #  체스판의 크기, 기사의 수, 명령의 수

    landform = [list(map(int, input().split())) for _ in range(L)]

    # 초기 기사 정보 입력받는다.
    knights = [Knight([i+1] + list(map(int, input().split()))) for i in range(N)]
    knights_map = {}
    for i in knights:
        knights_map[i.idx] = i

    knights_grid = [[0 for _ in range(L)] for _ in range(L)]
    for k in knights:
        for i, j in k.location:
            knights_grid[i][j] = k.idx

    # 왕의 명령 정보 입력 받는다.
    commands = [tuple(map(int, input().split())) for _ in range(Q)]

    for command in commands:
        command_from_king(command, knights_map, knights_grid, landform)

    """생존한 기사들이 받은 총 피해 계산"""
    result = 0
    for knight in knights:
        if knight.disabled:
            continue
        result += (knight.initial_health - knight.health)

    print(result)