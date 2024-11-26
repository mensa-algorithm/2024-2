# CURRENTCHANNEL = 100
# buttons = ['0','1','2','3','4','5','6','7','8','9']
# brokenButtons = []
# targetChannel = input()
# brokenButtonNumber = int(input())
# if brokenButtonNumber != 0:
#     brokenButtons = list(map(str ,input().split()))
# usableButtons = [button for button in buttons if button not in brokenButtons]
# # print("usableButtons: ", usableButtons)
# intUsableButtons = [int(button) for button in buttons if button not in brokenButtons]
# def setFlag(closestChannel):
#     if targetChannel[0] in usableButtons:
#         l = [abs(int(targetChannel[0]) - int(j)) for j in usableButtons]
#         closestChannel.append(usableButtons[l.index(min(l))])
#         return 'same'
#     else:
#         list = [abs(int(targetChannel[0]) - int(j)) for j in usableButtons]
#         if list.count(min(list)) == 2:
#             newList = list
#             minMin = usableButtons[newList.index(min(newList))]
#             newList[newList.index(min(newList))] = newList[newList.index(min(newList))] + 1
#             maxMin = usableButtons[newList.index(min(newList))]
#             # print("minMin: ",minMin,"maxMin: ",maxMin)
#             # print(abs(int(minMin + str(max(intUsableButtons)) * (len(targetChannel)-1))))
#             # print(abs(int(maxMin + str(min(intUsableButtons)) * (len(targetChannel)-1))))
#             # print(abs(int(minMin + str(max(intUsableButtons)) * (len(targetChannel)-1)) - int(targetChannel)))
#             # print(abs(int(maxMin + str(min(intUsableButtons)) * (len(targetChannel)-1))- int(targetChannel)))
#             if abs(int(minMin + str(max(intUsableButtons)) * (len(targetChannel)-1)) - int(targetChannel)) < abs(int(maxMin + str(min(intUsableButtons)) * (len(targetChannel)-1))- int(targetChannel)) :
#                 # print("minMin: ",minMin)
#                 closestChannel.append(minMin)
#                 return 'small'
#             else:
#                 # print("maxMin: ", maxMin)
#                 closestChannel.append(maxMin)
#                 return 'big'
#         if int(usableButtons[list.index(min(list))]) > int(targetChannel[0]):
#             l = [abs(int(targetChannel[0]) - int(j)) for j in usableButtons]
#             closestChannel.append(usableButtons[l.index(min(l))])
#             return 'big'
#         if int(usableButtons[list.index(min(list))]) < int(targetChannel[0]):
#             l = [abs(int(targetChannel[0]) - int(j)) for j in usableButtons]
#             closestChannel.append(usableButtons[l.index(min(l))])
#             return 'small'
# if len(usableButtons) == 0:
#     print(abs(int(targetChannel)-CURRENTCHANNEL))
# else:
#     if CURRENTCHANNEL - 2 <= int(targetChannel) <= CURRENTCHANNEL + 3:
#         print(abs(CURRENTCHANNEL - int(targetChannel)))
#     else:
#         closestChannel = []
#         flag = setFlag(closestChannel)
#         # print(flag)
#         # print(closestChannel)
#         for i in targetChannel[1:]:
#             if flag == 'small':
#                 # print(str(max([int(j) for j in usableButtons])))
#                 closestChannel.append(str(max([int(j) for j in usableButtons])))
#             if flag == 'big':
#                 closestChannel.append(str(min([int(j) for j in usableButtons])))
#             if flag == 'same':
#                 if i in usableButtons:
#                     closestChannel.append(i)
#                 else:
#                     list = [str(abs(int(i) - int(j))) for j in usableButtons]
#                     closestChannel.append(usableButtons[list.index(min(list))])
#         newClosestChannel = ''
#         for str in closestChannel:
#             newClosestChannel += str
#         # print("closestChannel: ", newClosestChannel)
#         print(len(targetChannel) + abs(int(newClosestChannel)-int(targetChannel)))
#
#
#
#
#
#
#
#
#
n = int(input())  # 이동하려는 채널
m = int(input())  # 고장난 버튼의 개수
broken = set(map(int, input().split()))  # 고장난 버튼 리스트

# 현재 채널에서 + 또는 - 버튼을 몇 번 눌러야 하는지 계산하는 함수
def possible(channel):
    if channel == 0:
        if 0 in broken:
            return 0
        else:
            return 1
    cnt = 0
    while channel > 0:
        if channel % 10 in broken:
            return 0
        cnt += 1
        channel //= 10
    return cnt

ans = abs(n - 100)  # 초기값: n에서 100까지 버튼을 누르는 횟수

# 0부터 1000000까지 모든 채널에 대해 가능한지 확인하고 최솟값을 갱신
for channel in range(1000001):
    cnt = possible(channel)
    if cnt > 0:
        press = abs(channel - n)
        if ans > cnt + press:
            ans = cnt + press

print(ans)
