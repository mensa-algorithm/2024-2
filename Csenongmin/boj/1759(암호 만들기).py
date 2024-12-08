import sys
input = sys.stdin.readline

L, C = map(int, input().split())
vowls = ['a', 'e', 'i', 'o', 'u']
password = input().split()
password.sort()

def valid(curr):
    vowls_count = 0
    for elem in curr:
        if elem in vowls:
            vowls_count += 1
    if vowls_count >= 1 and L - vowls_count >= 2:
        return True
    else :
        return False

def backtrack(curr):
    if len(curr) == L and valid(curr):
        result = ''.join(curr)
        ans.append(result)
        return
    for char in password:
        if char > curr[-1]:
            curr.append(char)
            backtrack(curr)
            curr.pop()




ans = []
for char in password:
    root = [char]
    backtrack(root)

print(*ans, sep='\n')
