# 문제를 보며 처음 한 단순한 생각 -> 시간 복잡도는 O(N^2)가 걸리기에 아이디어 파기
# def countElements(self, arr: List[int]) -> int:
#     count = 0
#     for x in arr:
#         if x + 1 in arr:
#             count += 1
#     return count

# 정답 풀이 코드
def countElements(self, arr: List[int]) -> int:
    answer = 0
    arr.sort()
    i=0 # slow pointer
    j=1 # fast pointer
    while j < len(arr):
        if arr[j] - arr[i] == 0:
            j += 1
        else:
            if arr[j]-arr[i] == 1:
                answer += 1
            i+=1

    return answer

# 두 개의 Slow, Fast 포인터를 두고
# 1. 두 포인터의 arr 값이 같으면 Fast Pointer + 1
# 2. 두 포인터의 arr 값의 차이가 1(우리가 찾는 값)이라면, answer + 1, Slow Pointer +1
# 3. 두 포인터의 arr 값의 차이가 0도, 1도 아니라면, 단순히 Slow Pointer

# 이 방식으로 문제를 해결하면, x 와 x + 1이 arr안에 각각 어떤 위치에 존재하던지 간에, x+1을 가진 x의 개수를 셀 수 있다.
# 그리고 If there are duplicates in arr, count them separately. 이 조건 또한 만족시킬 수 있다.
# 또한 while문을 통한 순회 시, 각각의 원소에 포인터가 머무를 수 있는 횟수는 최대 2번이기에, 최악의 경우더라도 시간복잡도 O(2N)로 끝낼 수 있다.




