import sys
input = sys.stdin.readline

N = int(input().strip())
stk = []
for _ in range(N):
    op = input().rstrip()
    if op =="top":
        if len(stk)==0:
            print(-1)
        else:
            print(stk[-1])  
    elif op=="pop":
        if len(stk)==0:
            print(-1)
        else:
            print(stk.pop())
    elif op=="size":
        print(len(stk))
    elif op=="empty":
        if len(stk)==0:
            print(1)
        else:
            print(0)
    else:
        push, n = op.split(" ")
        stk.append(int(n))