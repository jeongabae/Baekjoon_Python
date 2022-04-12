import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque([i for i in range(1,N+1)])

while True:
    a = queue.popleft()
    if not queue:
        print(a)
        break
    b = queue.popleft()
    queue.append(b)