n, k = map(int,input().split())
money_value = [int(input()) for _ in range(n)]
cnt = 0
for i in money_value[::-1]:
    while k//i>0:
        # k -= i
        cnt += k//i
        k %= i
print(cnt)
