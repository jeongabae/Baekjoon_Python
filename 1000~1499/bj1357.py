def rev(x):
    x = x[::-1]
    return x
X, Y = input().split()
print(int(rev(str(int(rev(X))+int(rev(Y))))))
"""다른분풀이 
print(int(str(sum(map(int,input()[::-1].split())))[::-1]))
"""
print(int(str(sum(map(int,input()[::-1].split())))[::-1]))
