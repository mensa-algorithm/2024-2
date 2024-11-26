# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

n = int(input())

dp = [0] * (n + 1)
def main():
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if n == 3:
        print(1)
        return
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        idx1 = i//3 if i%3==0 else 0
        idx2 = i//2 if i%2==0 else 0
        idx3 = i-1
        l = [dp[idx] for idx in [idx1,idx2,idx3] if idx != 0]
        dp[i] = min(l) + 1
    print(dp[n])
main()
