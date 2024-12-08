import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

ans_list = []
belt = [int(input().strip()) for _ in range(N)]
belt = belt + belt[:k+1]

start = 0
end = 0
sushi = {}

while True:
    if  end - start < k:  # k=4 일때 3
        if end == len(belt):
            break
        if belt[end] in sushi:
            sushi[belt[end]] += 1  # dict에 key = sushi name, value = number of sushi
        else:
            sushi[belt[end]] = 1
        end += 1
    
    else:
        if c in sushi:
            ans_list.append(len(sushi))
        else:
            ans_list.append(len(sushi)+1)       
        sushi[belt[start]] -= 1
        if sushi[belt[start]] < 1:  # 개수가 0개면 없애기
            del sushi[belt[start]]
        start += 1
        


print(max(ans_list))

