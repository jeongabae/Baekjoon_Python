import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
answer = ""

for i in range(N):
    parenthesis = input()
    cnt = 0
    for c in parenthesis:
        cnt += 1 if c == '(' else -1
        if cnt < 0:
            break
    print("YES" if cnt == 0 else "NO")


"""백준 1등분 코드
from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')
"""
"""내 풀이랑 비슷한 정석 답
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
result = ""

for i in range(N):
    testcase = input()
    cnt = 0
    for c in testcase:
        cnt += 1 if c == '(' else -1
        if cnt < 0:
            result += "NO\n"
            break
    else:
        result += "YES\n" if cnt == 0 else "NO\n"

print(result)
"""