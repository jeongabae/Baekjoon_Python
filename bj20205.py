n, k = map(int, input().split())
p = [list(map(str, input().split())) for i in range(n)]
# for i in range(n):
#     for j in range(k):
#         for m in range(n):
#             for _ in range(k):
#                 print(p[i][m], end=' ')
#         print()
for i in range(n):
    for j in range(k):
        print(*(p[i][m]*k for m in range(n)))
        print()
