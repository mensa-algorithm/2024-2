import collections

import numpy as np

golem_dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 골렘 클래스 만들자.
class Golem:
    def __init__(self, grid, center, entrance):
        # center는 1이런식으로 들어오니까...
        self.grid = grid # R x C 격자판
        self.center = (-2, center - 1) # 정령이 탑승한 중앙 위치
        self.locs = [(self.center[0] + dx, self.center[1] + dy) for dx, dy in golem_dxdy] # center를 제외하고 차지하고 있는 위치
        self.entrance = golem_dxdy[entrance] # 출구 위치(방향)

    def __repr__(self):
        return f"[Golem: center: {self.center}, locs: {self.locs}, entrance: {self.entrance}]"

    def is_in_grid(self, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def is_in_wall(self, x, y):
        return x < len(grid) and 0 <= y < len(grid[0])

    def is_golem_in_grid(self):
        cnt = 0
        for i, j in self.locs:
            if not self.is_in_grid(i, j):
                cnt += 1
        return cnt == 0

    def flush_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = 0

    def is_partially_out(self):
        x, y = self.center
        return x == -1
    def is_entirely_out(self):
        result = False
        for x, y in self.locs:
            if not self.is_in_grid(x, y):
                result = True
        return result
    def lookup_direction(self): # 어디로 이동할 수 있는지 유효성 검사
        """남쪽 방향 가능한지"""
        # 특수 케이스
        if self.is_entirely_out():
            x, y = self.locs[2] # 남 방향의 좌표만 뽑아서 검사
            if self.is_in_grid(x+1, y) and grid[x+1][y] == 0: # 다른 골렘이 없다면,
                return (1, 0) # 남쪽 방향으로 갈 수 있음을 알림

        # 일반적인 경우
        fail = False
        for i in range(1, 4):
            x, y = self.locs[i]
            if not self.is_in_grid(x+1, y) or not grid[x+1][y] == 0:
                fail = True
        if not fail:
            return (1, 0)

        """서쪽 방향 가능한지"""
        print("서쪽 유효성검사시작")
        temp_invalid = False
        nx, ny = self.locs[0]
        wx, wy = self.locs[3]
        sx, sy = self.locs[2]
        candidates = [(nx, ny - 1), (wx, wy - 1), (wx + 2, wy), (sx, sy - 1), (sx, sy - 2)]
        print(candidates)
        for i, j in candidates:
            if not self.is_in_wall(i, j):
                temp_invalid = True
                continue
            if self.is_in_grid(i, j):
                if not grid[i][j] == 0:
                    temp_invalid = True
        if not temp_invalid:
            return (0, -1)

        """동쪽 방향 가능한지"""
        print("동쪽 유효성검사시작")
        temp_invalid = False
        nx, ny = self.locs[0]
        ex, ey = self.locs[1]
        sx, sy = self.locs[2]
        candidates = [(nx, ny + 1), (ex, ey + 1), (ex + 2, ey), (sx, sy+1), (sx, sy+2)]
        for i, j in candidates:
            if not self.is_in_wall(i, j):
                temp_invalid = True
                continue
            if self.is_in_grid(i, j):
                if not grid[i][j] == 0:
                    temp_invalid = True
        if not temp_invalid:
            return (0, 1)

        return None

    def move(self, direction):
        dx, dy = direction
        """골렘 현 위치를 0으로 초기화"""
        for i, j in self.locs + [self.center]:
            if self.is_in_grid(i, j):
                self.grid[i][j] = 0
        """일반적인 로직 -> 위치 옮겨줌"""
        if dx == 1 and dy == 0: # 남쪽 방향
            x, y = self.center
            self.center = (x+1, y)
            temp = []
            for i, j in self.locs:
                temp.append((i+1, j))
            self.locs = temp
        """서, 동 방향인 경우 출구 회전 처리"""
        if dy == 1: # 동쪽 방향
            x, y = self.center
            print(f"출구 동쪽으로 회전! 기존: {self.entrance}", end='')
            idx = golem_dxdy.index(self.entrance)
            self.entrance = golem_dxdy[(idx + 1) % 4]
            print(", 이후: ", self.entrance)
            self.center = (x + 1, y + 1)
            temp = []
            for i, j in self.locs:
                temp.append((i + 1, j + 1))
            self.locs = temp
        elif dy == -1: #서쪽 방향
            x, y = self.center
            print(f"출구 서쪽으로 회전! 기존: {self.entrance}", end='')
            idx = golem_dxdy.index(self.entrance)
            self.entrance = golem_dxdy[(idx - 1) % 4]
            print(", 이후: ", self.entrance)
            self.center = (x + 1, y - 1)
            temp = []
            for i, j in self.locs:
                temp.append((i + 1, j - 1))
            self.locs = temp
        """움직인 이후 골렘 현 위치를 grid에 표기"""
        for x, y in self.locs + [self.center]:
            if self.is_in_grid(x,y):
                self.grid[x][y] = 1
        # self.grid[self.entrance[0]][self.entrance[1]] = 2
        print(np.array(self.grid))

    def pointInMe(self, x, y):
        for i, j in self.locs + [self.center]:
            if i== x and j == y:
                return self
        return None
def search(cur_golem, grid, golems):
    cen_x, cen_y = cur_golem.center
    ex, ey = cur_golem.entrance
    x = cen_x + ex
    y = cen_y + ey

    q = collections.deque([cur_golem])
    solve=[]
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]

    while q:
        searching_golem = q.popleft()

        for dx, dy in golem_dxdy:
            nx = x + dx
            ny = y + dy
            if nx == cen_x and ny == cen_y: # 자기 자신 중심 쪽은 탐색에서 제외
                continue
            print(f"searching_golem: {searching_golem}")
            if not searching_golem.is_in_grid(nx, ny):
                continue
            print(nx, ny)
            print("현재 골렘 출구 방향:", searching_golem.entrance)
            if grid[nx][ny] == 1 and not visited[nx][ny]: # 다른 골렘 발견 시
                print(f"정령이 남하 중 다른 골렘을 {nx, ny}에서 발견했다.")
                visited[nx][ny]=True
                for g in golems:
                    new_golem = g.pointInMe(nx, ny)
                    if new_golem:
                        print(f"new_golem: {new_golem}")
                        q.append(new_golem) # 현재 탐색 골렘을 갱신해 줌
            else:
                solve.append(searching_golem.locs[2][0])
    return solve



def try_move_golem(golem, golems, grid):
    # while 문 돌거야
    direction = golem.lookup_direction()
    while direction:
        golem.move(direction)
        direction = golem.lookup_direction()
        print(f"direction: {direction}")


    if not golem.is_golem_in_grid():
        # 골렘의 위치가 숲 밖이거나, 걸쳐있다면, grid전부 날리고 이번 턴은 종료
        golem.flush_grid()
        print("ㅈ망한 판이니까 초기화")
        return 0
    else:
        # 골렘이 숲안이라면, 정령이 남쪽으로 탐색 시작
        res = search(golem, grid, golems)
        return max(res) + 1

if __name__ == '__main__':
    R, C, K = map(int, input().split())

    grid = [[0 for _ in range(C)] for _ in range(R)]

    golems = []

    result = 0

    print(np.array(grid))
    for i in range(K): # 골렘 정보
        center_col, entrance_num = map(int, input().split())
        golems.append(Golem(grid, center_col, entrance_num))

    for i, golem in enumerate(golems):
        print(f"golem {i+1} moving start")
        res = try_move_golem(golem, golems, grid)
        print(f"res: {res}")
        result += res
        print(np.array(grid))
        print("---------------------")

    # print(np.array(grid))

    # test = golems[0].lookup_direction()
    print(f"result: {result}")