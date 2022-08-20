while 1:
    s = input()
    if s == '#':
        break
    cnt = 0
    for i in s:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)