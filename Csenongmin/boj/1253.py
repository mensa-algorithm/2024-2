import sys

input = sys.stdin.readline
N = int(input().strip())

num = list(map(int, input().split()))
num.sort()

good = 0


for i in range(N):
    temp = num[:i] + num[i+1:]
    start, end = 0, len(temp)-1

    while start < end: # 투 포인터 알고리즘
        addition = temp[start] + temp[end]
        if addition == num[i]:
            good += 1
            break
        elif addition < num[i]:
            start += 1
        else :
            end -= 1

print(good)