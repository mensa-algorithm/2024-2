import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

#거리 1로 초기화
for i in range(D):
    graph[i].append((i+1,1)) #[next_node, cost]

#지름길 업데이트
for _ in range(N):
    s, e, length = map(int, input().split())
    if e > D:  #고려안함
        continue
    graph[s].append((e,length))

dijkstra(0)
print(distance[D])