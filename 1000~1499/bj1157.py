a = input().upper()
al = list(set(a))
cnt = []
print(al)
for i in al:
    count = a.count(i)
    print('i',i)
    print('count i :', count)
    cnt.append(count)
    print('cnt:', cnt)
print('?' if cnt.count(max(cnt)) >= 2 else a[cnt.index(max(cnt))])
