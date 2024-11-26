n=int(input()) # <=500

twoCount = 0
fiveCount = 0

for i in range(1, n+1):
    while True:
        if i % 5 == 0:
            i = i//5
            fiveCount += 1
        else:
            break
    while True:
        if i % 2 == 0:
            i = i//2
            twoCount += 1
        else:
            break
if twoCount >= fiveCount:
    print(fiveCount)
else:
    print(twoCount)
