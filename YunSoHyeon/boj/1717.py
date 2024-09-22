# 입력되는 두 원소가 같은 집합에 속해있는지 확인하는 문제입니다.

import sys
sys.setrecursionlimit(10**6) # 재귀 호출 깊이 제한
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n + 1)] 

# 경로 압축 Union-find
def find(num):
    if parent[num] != num:
        parent[num] = find(parent[num])
    
    return parent[num]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    # print(parent)
    op, a, b = map(int, input().split())
    if op == 0: 
        union(a, b)
    else: 
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
