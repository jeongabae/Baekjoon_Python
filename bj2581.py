# M = int(input())
# N = int(input())
# n = []
# for i in range(M,N+1):
#     if i == 1:
#         continue
#     n.append(i)
#     for j in range(2, i):
#         if i % j == 0:
#             n.remove(i)
#             break
# if n:
#     print(sum(n))
#     print(min(n))
# else:
#     print(-1)
M = int(input())
N = int(input())
n = []
for i in range(M,N+1):
    is_ok = 1
    if i!=1:
        for j in range(2, i):
            if i % j == 0:
                is_ok = 0
                break
        if is_ok:
            n.append(i)
if n:
    print(sum(n))
    print(min(n))
else:
    print(-1)