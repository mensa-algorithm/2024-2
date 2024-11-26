from collections import deque
def DFS(graph , v, visited):

    visited[v] = True
    print(v, end=' ')

    for i in sorted(graph[v]):
        if not visited[i]:
            DFS(graph, i ,visited)
def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N , M , V = map(int, input().split(" "))

graph = [[] for _ in range(N+1)]

for i in range(M):
    nodeOne , nodeTwo = map(int, input().split())
    graph[nodeOne].append(nodeTwo)
    graph[nodeTwo].append(nodeOne)

visitedForDFS = [False] * (N+1)
visitedForBFS = [False] * (N+1)

DFS(graph,V,visitedForDFS)
print()
BFS(graph,V,visitedForBFS)

