
import sys
input = sys.stdin.readline

test_case = int(input())
for i in range(test_case):
    applicant = int(input())
    data = []
    # 1차 서류 심사, 2차 면접을 통해 신입사원을 채용한다.
    for _ in range(applicant):
        paper, interview = map(int, input().split()) # 서류 심사와 면접 심사에 대한 등수가 주어진다.
        data.append((paper, interview))  
    data.sort()  # 지원자 A가 지원자 B보다 서류 결과와 면접 결과 모두 떨어지면 A는 결코 채용될 수 없으므로, 일단 서류를 기준으로 오름차순 정렬한다.

    new = 1  # 서류 심사 결과 1위인 지원자는 무조건 선발이 됩니다. 
    winner = data[0][1]
    for paper, interview in data:
        if interview < winner:  # 서류 심사에서 등수가 뒤처지는 경우에는 면접 심사 등수가 더 높아야지만 채용된다. (등수가 높다 = 숫자가 작다)
            winner = interview # 합격자 면접 순위 업데이트
            new += 1

    print(new)
    
