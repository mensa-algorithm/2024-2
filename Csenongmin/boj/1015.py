import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

# B[P[i]] = A[i]
P = [-1]*N
B = sorted(A[:])

for i in range(N):
    j = A.index(B[i])
    A[j] = -1
    P[j] = i

for elem in P:
    print(elem, end=" ")


        