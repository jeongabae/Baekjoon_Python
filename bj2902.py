for i in input().split('-'):
    print(i[0], end='')
"""다른분풀이 
print(*filter(str.isupper,input()),sep="")
"""
"""다른분풀이2
print(''.join(filter(str.isupper,input())))
"""