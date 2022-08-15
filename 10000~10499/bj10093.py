# 백준 10093번 : 숫자 : 구현
a, b = map(int, input().split())
a2 = min(a, b)
b2 = max(a, b)
n = b2-a2-1

if b2-a2<=1:
    n=0

print(n)
ans = [i for i in range(a2+1, b2)]
print(*ans)