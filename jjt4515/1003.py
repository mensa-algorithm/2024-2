# 2024/10/13 
# dp
# 백준 1003번 피보나치 함수: https://www.acmicpc.net/problem/1003
# 접근 방법: n에 대해 n-2와 n-1의 각 0과 1출력 횟수를 구하고 이를 더해주면 된다.

t = int(input())

lst = [(1,0),(0,1)]
for i in range(2, 41):
    zero = lst[i-1][0] + lst[i-2][0]
    one = lst[i-1][1] + lst[i-2][1]
    lst.append((zero, one))

input_lst = []
for _ in range(t):
    input_lst.append(int(input()))

for n in input_lst:
    for i in range(2):
        print(lst[n][i], end=" ")
    print()
