# 9/22 
# dp
# 백준 2096번 내려가기: https://www.acmicpc.net/problem/2096
# 초기 접근방법: 위에서 아래로 반복문을 돌며 min_graph에는 이전까지의 최소 + 현재 값을 더한 값을 저장하고
# max_graph에는 이전까지의 최대 + 현재 값을 더한 값을 저장하여 최종적으로 최대, 최소를 찾는다.
# 이 방식으로 했더니 메모리 초과가 났다.
# 다음 접근방법: min_graph와 max_graph를 1차원 리스트로 변경했다. 이마저도 메모리 초과가 나서 입력 받는 것도 따로 2차원 배열에 저장되지 않도록
# 수정했다.

n = int(input())

inp = list(map(int, input().split()))
min_list = inp 
max_list = inp

for i in range(n-1):
    inp = list(map(int, input().split()))
    min_list = [inp[0]+min(min_list[0], min_list[1]), inp[1]+min(min_list), inp[2]+min(min_list[1], min_list[2])]
    max_list = [inp[0]+max(max_list[0], max_list[1]), inp[1]+max(max_list), inp[2]+max(max_list[1], max_list[2])]

print(max(max_list), min(min_list))
