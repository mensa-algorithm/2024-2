dp_table = [[0,0] for i in range(41)]
dp_table[0] = [1,0]
dp_table[1] = [0,1]
def dp(n):
    for i in range(n+1):
        if dp_table[i] == [0,0]:
            dp_table[i][0] = dp_table[i-1][0] + dp_table[i - 2][0]
            dp_table[i][1] = dp_table[i - 1][1] + dp_table[i - 2][1]

number = int(input())
for i in range(number):
    dp_table = [[0, 0] for i in range(41)]
    dp_table[0] = [1, 0]
    dp_table[1] = [0, 1]
    n = int(input())
    dp(n)
    print(dp_table[n][0], dp_table[n][1])


