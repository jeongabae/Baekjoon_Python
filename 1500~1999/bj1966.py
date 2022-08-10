from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    important = deque(map(int,input().split()))
    cnt = 0
    while important:
        first = max(important)
        m -= 1
        pop = important.popleft()
        if first != pop:
            important.append(pop)
            if m < 0:
                m = len(important)-1
        else:
            cnt+=1
            if m == -1:
                print(cnt)
                break
