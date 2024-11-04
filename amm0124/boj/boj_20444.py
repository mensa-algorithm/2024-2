# 백준 20444 문제 링크 : https://www.acmicpc.net/problem/20444
# 가로로 a번, 세로로 b번 잘랐을 때 자른 횟수를 n1이라고 하면 : a + b = n1
# 색종이의 수 (a+1)(b+1) = ab+a+b+1 = ab+n1+1 개 
# 즉 색종이의 수는 가로로 a와 b에만 영향을 받음
# k = (a+1)(b+1) = ab+a+b+1 = ab+n+1

# 가로로 a번 , 세로로 b번 자르면 총 사각형 수는 (a+1)(b+1) = k임.
# x^2 -nx + (k-n-1) = 0 이차방정식의 판별식 d가 근을 양수인 실근을 가져야 함


import sys
n,k=map(int,sys.stdin.readline().split())

d=(n+2)**2-4*k # 판별식 
if d<0 :
    print("NO")
else : #d>=0 
    if int(d**0.5)**2!=d :
        print("NO")
    else : #정수형
        t=int(d**0.5)
        if k-n>=1 : 
            if n%2==0 and t%2==0 :
                print("YES")
            elif n%2!=0 and t%2!=0 :
                print("YES")
            else :
                print("NO")
        else :
            print("NO")
