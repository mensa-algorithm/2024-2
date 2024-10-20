# 2024/10/20 
# 수학, 그리디, 문자열
# 백준 1541번 잃어버린 괄호: https://www.acmicpc.net/problem/1541
# 접근 방법: 값을 최소로 만들기 위해서는 -를 최대화 하면 된다. 그래서 - 단위로 끊고, 그 안의 수들을 다 더했다.
# 이후 - 연산까지 계산해줘서 답을 구했다

lst = input().split('-')
ans = 0
for i in range(len(lst)):
    node = lst[i]
    subans = 0
    sublst = node.split('+')
    for subnode in sublst:
        subans += int(subnode)
    if i == 0:
        ans += subans
    else:
        ans -= subans
print(ans)
