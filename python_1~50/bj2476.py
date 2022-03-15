a_list = []
b_list = []
c_list = []
money = []
n = int(input())
for _ in range(n):
    a, b, c = map(int,input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    if a==b==c: money.append(10000+a*1000)
    elif a==b or a==c: money.append(1000+a*100)
    elif b==c: money.append(1000+b*100)
    else: money.append(max(a,b,c)*100)
print(max(money))
