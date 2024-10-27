
import sys
input = sys.stdin.readline

D, K = map(int, input().split())

coeff = [[1, 0]]
coeff.append([0, 1])

for i in range(1, D) :
    coeff.append([coeff[i - 1][0] + coeff[i][0], coeff[i - 1][1] + coeff[i][1]])

for i in range(1, K) :
    for j in range(1, K) :
        if i * coeff[D - 1][0] + j * coeff[D - 1][1] == K :
            print(i)
            print(j)
            exit(0)
           

            
