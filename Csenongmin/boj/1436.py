import sys
input = sys.stdin.readline

N = int(input().strip())
endGame = '666'
answer = []

count = 0
i = 0
while True:
    index = str(i).find(endGame)
    if index != -1:
        answer.append(i)
    if len(answer) == N:
        break
        
    i += 1
print(answer[N-1])