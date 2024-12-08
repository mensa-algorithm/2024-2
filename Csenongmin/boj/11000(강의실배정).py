import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

#시작시간 순서로 정렬
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort()

#종료시간 우선순위 큐에 삽입
q = []
heapq.heappush(q, lecture[0][1])

for i in range(1, n):
    if lecture[i][0] >= q[0]:
        heapq.heappop(q)  #같은 강의실 사용
    heapq.heappush(q, lecture[i][1])


print(len(q))