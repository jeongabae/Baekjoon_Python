# n, m = map(int, input().split())
# a = [input() for _ in range(n)] # 가로로 더함
# a += zip(*a) #세로로 더함
# re = ['UP', 'DOWN', 'LEFT', 'RIGHT']
# c = 0
# for i in a:
#     i = ''.join(i)
#     if '#.#' in i:
#         print(re[c])
#     if '##' in i: #한 변 넘어감.
#         c += 1
n, m = map(int, input().split())
a = [input() for _ in range(n)] # 가로로 더함
# print(a)
a += zip(a) #세로로 더함
print(a)
