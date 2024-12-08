import sys
input = sys.stdin.readline
N = int(input().strip())
A = list(map(int,input().split()))
M = int(input().strip())
arr = list(map(int,input().split()))
A.sort()
#arr각 원소별로 이분탐색
for num in arr:
    lt, rt = 0, N-1
    isExist = False

    while lt <= rt:
        mid = (lt+rt)//2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    if not isExist:
        print(0)