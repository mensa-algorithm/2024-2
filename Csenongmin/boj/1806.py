import sys
from collections import deque
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

len_list = []
queue = deque()

queue.append(num[0])
i = 1

if sum(num) < S: # S이상 불가능하면 0출력
    print(0)
    exit()

ps = queue[0]
while queue: # 투포인터로도 가능
    if ps < S:
        if i == N:
            break
        queue.append(num[i])
        ps += num[i]
        i += 1
        
    else : # sum(queue) >= S
        len_list.append(len(queue))
        ps -= queue[0]
        queue.popleft()  
        if len(queue) == 0 and i != N:
            queue.append(num[i])
            ps += num[i]
            i += 1

    
print(min(len_list))
