import sys
input = sys.stdin.readline
N = int(input().strip())
S = set([])
for i in range(N):
    a = input().strip()
    if a == 'all':
        S = set([x for x in range(1,21)])
    elif a == 'empty':
        S = set([])
    else:
        op, num = a.split()
        num = int(num)
        if op == 'add':
            S.add(num)
        elif op == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif op == 'remove':
            if num in S:
                S.remove(num)
        elif op == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
        
   
    