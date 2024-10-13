# 백준 1079 마피아
# 재귀를 이용한 dp - memoization 사용
# 현재 상황을 dictionary의 key로 memo하고 현재 상황이 존재한다면 
# 불러오는 형태로 시간 복잡도를 줄였습니다.

import sys
import math

sys.setrecursionlimit(10**9)

def mafia(n, crime, flag, acc, memo):
    global r, eunjin, answer

    if n <= 1:
        answer = max(answer, acc)
        return

    if (n, tuple(crime), flag) in memo:
        return

    memo[(n, tuple(crime), flag)] = True

    if n % 2 == 0:
        acc += 1
        for i in range(len(crime)):
            crime_list = crime[:]
            if i == eunjin or crime_list[i] == (-1) * math.inf:
                continue

            crime_list[i] = (-1) * math.inf

            for j in range(len(crime_list)):
                if j != i or crime_list[j] != (-1) * math.inf:
                    crime_list[j] += r[i][j]

            max_index = crime_list.index(max(crime_list))
            
            if max_index == eunjin:
                answer = max(answer, acc)
            else:
                crime_list[max_index] = (-1) * math.inf
                mafia(n - 2, crime_list, flag, acc, memo)
    else:
        max_index = crime.index(max(crime))

        if max_index == eunjin:
            return 0
        else:
            crime_list = crime[:]
            crime_list[max_index] = (-1) * math.inf
            mafia(n - 1, crime_list, flag, 0, memo)

n = int(input())
crime = list(map(int, input().split()))
r = [[0] * n for _ in range(n)]

for _ in range(n):
    r[_] = list(map(int, input().split()))

eunjin = int(input())
answer = 0
flag = False
memo = {}

mafia(n, crime, flag, 0, memo)
print(answer)
