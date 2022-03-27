import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    X = 0
    cmd = sys.stdin.readline().split()

    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]
    if cmd == "push":
        stack.append(X)
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0 if len(stack) else 1)
    elif cmd == "top":
        print(-1 if len(stack)==0 else stack[-1])

"""다른 분 풀이. 내 풀이와 비슷한데 input을 함수로 사용하신것은 아이디어 좋으신것 같다.(짧게 짤 수 있으니..!)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack = []

for i in range(N):
    cmd = input().split()
    X = 0
    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        stack.append(X)
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0 if len(stack) else 1)
    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
"""