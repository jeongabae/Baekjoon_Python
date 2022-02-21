n = int(input())
for i in range(n):
    p = int(input())
    dic = {}
    for j in range(p):
        x, y = map(str, input().split())
        dic[int(x)] = y
    print(dic[max(dic.keys())])
