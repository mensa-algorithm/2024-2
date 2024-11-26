arr = [1, 2, 3, 4]

# 현재 인덱스 +1 만큼을 매개변수로 계속 넘겨주어야 함
# 순서가 상관없고 중복 불가이기 때문에 현재 인덱스보다 같거나 작은 인덱스는 볼 필요가 없기 때문
def combinations(n, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


combinations(2, [], 0)