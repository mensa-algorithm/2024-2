import sys
input = sys.stdin.readline
#스택으로 수엶만들기
N = int(input().strip())
stack = []

num = [int(input().strip()) for _ in range(N)]
j=2
ans = ['+']
minus = 0
stack.append(1)

for i in range(N):
    if len(stack)==0:
         stack.append(j)
         j+=1
         ans.append('+')
    if stack[-1] > num[i]:
            ans = ["NO"]
            break
    while stack[-1] < num[i]:
        stack.append(j)
        j+=1
        ans.append('+')
    n = stack.pop()
    ans.append('-')

for el in ans:
     print(el)


    

    