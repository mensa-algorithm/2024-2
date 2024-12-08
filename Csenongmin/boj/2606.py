import sys
input = sys.stdin.readline

#유니온 파인드란?
# 유니온 파인드는 그래프 알고리즘으로 두 노드가 같은 그래프에 속하는지 판별하는 알고리즘입니다.
# 노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산으로 이루어집니다.

#특정 원소가 속한 집합을 찾기
def find(parent, x):
    #루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]  # 최종 부모 노드 출력

#두 원소가 속한 집합을 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input().strip())
v = int(input().strip())
parent = [i for i in range(n+1)] #부모 테이블 초기화
#union 수행
for i in range(v):
    a, b = map(int, input().split())
    union(parent,a,b)


ans = 0

for i in range(1, n+1):
    if find(parent, i) == 1:
        ans += 1

print(ans-1)

