n = int(input())
line = [int(input()) for _ in range(n)]
m, s, a = 1, [], []

for i in line:
    while not s or s[-1] < int(i):
        a.append('+')
        s.append(m)
        m += 1
    if s[-1] > int(i):
        print('NO')
        break
    else:
        a.append('-')
        s.pop()

print('\n'.join(a))
