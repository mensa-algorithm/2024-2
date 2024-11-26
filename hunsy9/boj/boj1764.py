n, m = map(int, input().split())
nlist=set()
mlist=set()
for i in range(n+m):
    if i < n:
        nlist.add(input())
    else:
        mlist.add(input())
interSet = sorted(list(nlist&mlist))
print(len(interSet))
for j in interSet:
    print(j)