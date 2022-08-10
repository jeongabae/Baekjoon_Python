K = int(input())
for i in range(K):
    n = sorted(list(map(int,input().split()))[1::])[::-1]
    gap = [n[j]-n[j+1] for j in range(len(n)-1)]
    print("Class",i+1)
    print("Max %d, Min %d, Largest gap %d"%(max(n),min(n),max(gap)))

"""다른분풀이
for i in range(int(input())):t=sorted([*map(int,input().split())][1:]);print(f'Class {i+1}\nMax {max(t)}, Min {min(t)}, Largest gap',max([w-v for v,w in zip(t,t[1:])]))
"""
"""다른분풀이
for i in range(int(input())):a=sorted(map(int,input().split()[1:]));print('Class %d\nMax %d, Min %d, Largest gap %d'%(i+1,a[-1],a[0],max([a[i+1]-a[i]for i in range(len(a)-1)])))
"""