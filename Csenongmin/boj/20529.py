import sys

def checkDiffrence(a , b):
    total=0
    for i in range(4):
        if a[i] != b[i]:
            total += 1
    return total
        
TestCase = int(sys.stdin.readline().strip())

for _ in range(TestCase):
    n = int(sys.stdin.readline().strip())
    mbti_list=sys.stdin.readline().split()
    #print(mbti_list)
    if n >= 33:
        print(0)
        continue
    ans = 99999

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                #if k > n: break
                total = checkDiffrence(mbti_list[i], mbti_list[j]) + checkDiffrence(mbti_list[j], mbti_list[k]) + checkDiffrence(mbti_list[i], mbti_list[k])
                #print(total)
                ans = min(total, ans)
                
    print(ans)    