import sys   # deque, string replace(old, new)
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    op = input().strip()
    n = int(input().strip())
    li = input().strip()

    if n!=0:
        li = deque(map(int, li[1:-1].split(",")))
    else:
        li = deque([])

    flag = True
    start = True
    for word in op: 
        if word == "R":
            start = not start
            
        elif word == "D":
            if len(li) == 0:
                print("error")
                flag = False
                break
            else:
                if start: 
                    li.popleft()
                else:
                    li.pop()
    if flag:
        if start:
            li = str(list(li))
            print(li.replace(" ",""))
        else:
            li.reverse()
            li = str(list(li))
            print(li.replace(" ",""))