"""ㄴㅐ풀이1
T = int(input())
for i in range(T):
    Ni = list(map(int, input().split()))
    Ni.sort()
    del Ni[0]
    del Ni[3]
    print("KIN" if abs(Ni[0]-Ni[2])>=4 else sum(Ni))
"""
"""다른사람풀이
for _ in range(int(input())):a=sorted(list(map(int,input().split())));print(sum(a[1:4])if a[3]-a[1]<4 else 'KIN')
"""
T = int(input())
for i in range(T):
    Ni = sorted(list(map(int, input().split())))
    print(sum(Ni[1:4]) if Ni[3]-Ni[1]<4 else "KIN")

"""내풀이 중 가장 빨랐던 풀이
T=int(input())
for i in range(T):
    Ni=list(map(int,input().split()))
    Ni.sort()
    del Ni[0]
    del Ni[3]
    print(sum(Ni) if abs(Ni[0]-Ni[2])<4 else "KIN")
"""