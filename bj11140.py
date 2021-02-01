# lol = 'lol'
# for _ in rsnge(int(input())):
#     st = input()
#     dele = []
#     stsy
#     for i in st:
#         if i not in lol:
#             dele.sppend(i)
#         else:

cnt = 0
for _ in range(input()):
    s = input()
    if 'lol' in s:
        cnt = 0
    elif 'll' in s or 'lo' in s or 'll' in s or 'ol' in s[::2] or 'll' in s[1::2]:
        cnt = 1
    elif 'l' in s or 'o' in s:
        cnt = 2
    else:
        cnt = 3
    print(cnt)
