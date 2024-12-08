import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())

# def quick_sort(arr):  # 퀵정렬 시간 초과
#     def sort(low, high):
#         if high <= low:
#             return

#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)

#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low

#     return sort(0, len(arr) - 1)

heapLeft = []
heapRight = []

for i in range(N):
    num = int(input().strip())

    if len(heapLeft) == len(heapRight):
        heapq.heappush(heapLeft, (-num, num))  # heapLeft의 루트값이 중간값이 되게끔 설정
    else:
        heapq.heappush(heapRight, (num, num)) # heapRight는 최소힙, heapLeft는 최대힙으로 만들면 됨.

    if heapRight and heapLeft[0][1] > heapRight[0][0]: # 최대힙의 루트값보다 최소힙의 루트값이 작을 경우 두 값을 바꿔준다.
        leftValue = heapq.heappop(heapLeft)[1]
        rightValue = heapq.heappop(heapRight)[0]

        heapq.heappush(heapLeft, (-rightValue, rightValue))
        heapq.heappush(heapRight, (leftValue, leftValue))

    print(heapLeft[0][1]) # 중간값 출력

        
 