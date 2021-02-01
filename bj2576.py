odd = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        odd.append(n)
if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))

# 6번째 줄부터 끝까지를 이렇게 쓸 수도 있음.
# if len(rs):
#     print(sum(rs))
#     print(min(rs))
#
# else:
#     print(-1)
