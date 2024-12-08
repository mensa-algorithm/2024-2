import sys
input = sys.stdin.readline

a, b = map(int, input().split())
one_sum = [0 for _ in range(60)]

# def bitCount(x):  시간초과
# 	if x == 0: return 0
# 	return x % 2 + bitCount(x//2)

def f(num):
    cnt = 0
    bin_num = bin(num)[2:] #0b제외 리스트화
    length = len(bin_num)  # 2의 몇 제곱 자리?
    for i in range(length):  # 최상위 비트부터 시작
        if bin_num[i] == "1":
            val = length-i-1  # 최상위 비트 제외 아래 비트들은 반복됨.
            cnt += one_sum[val]

            cnt += num-2**val + 1  # 최상위 비트의 1의 개수
            num = num - 2**val  # 다음 비트들 확인을 위해 num 업데이트
    return cnt



for i in range(1, 60):
    one_sum[i] = 2 ** (i-1) + 2 * one_sum[i-1]  # 2의 i자리 수까지의 누적합

print(f(b) - f(a-1))