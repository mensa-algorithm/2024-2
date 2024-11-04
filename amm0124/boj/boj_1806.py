# boj 1806번 부분합
# 문제 링크 : https://www.acmicpc.net/problem/1806
# 투포인터 문제 : start, end index 사용
# S가 될 때 까지 계속 합을 구함
# S가 넘어가면 start index를 넘길 때 까지 하나씩 올림. 
# 이러한 방식을 계속 사용 -> 2N의 시간에 해결 가능
# 시간 복잡도 O(n)

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_ = arr[0]
ans = 100001

while True:
    if sum_ < S:
        end += 1
        if end == N: break
        sum_ += arr[end]
    else: #sum_ >= S
        sum_ -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1
        
print(ans if ans != 100001 else 0)
