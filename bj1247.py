import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(3):
    N = int(input())
    l = [int(input()) for i in range(N)]
    if sum(l) == 0:
        print("0")
    elif sum(l) > 0:
        print("+")
    else:
        print("-")