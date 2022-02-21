score = [sum(map(int,input().split())) for i in range(5)]
a = max(score)
print("%d %d" %(score.index(a)+1, a))
