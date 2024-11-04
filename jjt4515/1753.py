# 2024/10/27
# 다익스트라
# 백준 1753번 최단경로: https://www.acmicpc.net/problem/1753
# 접근 방법: 최단경로 문제이므로 다익스트라 알고리즘을 적용한다.
# 다익스트라 알고리즘에서는 우선순위 큐를 사용한다.
# 힙에서 원소를 뺄 떄 방문처리하는 것보다 힙에 원소를 넣을 때 방문처리를 하니까 시간이 더 적게 걸렸다.

import heapq
from sys import stdin  

v, e = map(int, stdin.readline().split())
k = int(stdin.readline())

graph = [[] for _ in range(v+1)]
visited = [float('inf')] * (v+1)

for _ in range(e):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v,w))

# 다익스트라 알고리즘
def dijkstra(start):
    pQueue = []
    heapq.heappush(pQueue, (0,start))  #우선순위 큐 사용(거리, 노드)
    visited[start] = 0

    while pQueue:
        cost, s = heapq.heappop(pQueue)
 
        if visited[s] < cost:
            continue

        for v, w in graph[s]:
            if visited[v] > cost+w: # 비용 더 들면 무시
                visited[v] = cost+w
                heapq.heappush(pQueue, (cost+w, v))

dijkstra(k)
    
for i in range(1, len(visited)):
    if visited[i] == float('inf'):
        print("INF")
    else:
        print(visited[i])
    
