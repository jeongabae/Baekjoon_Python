T = int(input())
for i in range(T):
    n = int(input())
    print("Pairs for %d: " %n, end='')
    for j in range(1,(n+1)//2):
        if j!=1:
            print(", ",end='')
        print(j,n-j,end='')
    print()
"""다른 사람 풀이
T = int(input())
for _ in range(T):
    n = int(input())
    ls = []
    for i in range(1, (n+1)//2):
        ls.append('%d %d' % (i, n-i))
    print('Pairs for %d: %s' % (n, ', '.join(ls)))
"""
"""다른 사람 풀이
for i in range(int(input())):
    n=int(input())-1
    l=[]
    for j in range(n//2):
        l.append(str(j+1)+' '+str(n-j))
    print('Pairs for {}:'.format(n+1),(', ').join(l))
    """