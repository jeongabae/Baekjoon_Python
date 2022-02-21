# N = int(input())
# dot = 0
# for i in range(N+1):
#     for j in range(i+1):
#         dot += i + j
#         print(i, j, i+j)
# print(dot)
N = int(input())
dot = 0
for i in range(N+1):
    for j in range(i, N+1):
        dot += i + j
print(dot)
"""1등 분 코드인데 아직 이해하지 못했다..
N = int(input())
print((N * (N+1) * (N+2))//2)
"""