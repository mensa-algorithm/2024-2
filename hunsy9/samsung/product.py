arr = [1, 2, 3, 4]
def product(n, new_arr):
    global arr
    # 순서 상관 0, 중복 0
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

product(2, [])