n, x = map(int, input().split())
score = [i for i in input().split() if int(i) < x]
print(' '.join(score))
