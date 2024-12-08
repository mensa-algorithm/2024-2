import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b
    
N = int(input().strip())
dist = [[1000] * (N+1) for _ in range(N+1)]
parent = [ i for i in range(N+1)]
for _ in range(N-1):
    a, b, k = map(int, input().split())
    union(parent, a,b)
    dist[a][b] = k
