import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = [input().strip() for _ in range(N)]
result = []

for a in range(N-7):
    for b in range(M-7):
        w_index = 0 # w시작
        b_index = 0 # b시작
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2==0: #인덱스 짝수일땐 시작 문자와 같다
                    if chess[i][j] == 'W' : 
                        b_index += 1 # 일일이 바꿀필요 없음
                    else :
                        w_index += 1
                else: #인덱스 홀수 일때는 시작 문자와 달라야 한다
                    if chess[i][j] == 'W':
                        w_index += 1
                    else:
                        b_index += 1
        result.append(w_index)
        result.append(b_index)

print(min(result))
    
