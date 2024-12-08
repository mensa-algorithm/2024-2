import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0 #시작점 거리 0으로 설정
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        for i in graph[now]:
            time = dist + i[1]
            if time < distance[i[0]]:
                distance[i[0]] = time
                heapq.heappush(q, (time, i[0]))
   

N, M, X = map(int, input().split())
distance_X = [INF] * (N+1)

graph = [[] for _ in range(N+1)]
# for i in range(N):
#     graph[i].append((i+1,1)) #[next_node, time]

for _ in range(M):
    s, e, time = map(int, input().split())
    graph[s].append((e, time))

dijkstra(X, distance_X)
distance_X[0] = 0

for i in range(1,N+1):
    if i == X:
        continue
    distance = [INF] * (N+1)
    dijkstra(i,distance)
    distance_X[i] += distance[X]
    
print(max(distance_X))

#이렇게 하는 것 보다는 X로 갈 때, X로 올 떄 기준 다익스트라를
# 두 번하여 결과값을 더하는 것이 더 효율적.
#graph1[end].append([cost,start]) # 갈 때
#graph2[start].append([cost,end]) # 올 때 X 기준으로 다익스트라 알고리즘 ->2VlogE