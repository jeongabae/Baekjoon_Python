# 백준 1009번 : 분산처리 : 수학 (간단하게 생각하면 안 풀리는 문제)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    aa=a%10

    if aa == 0: # 패턴 1
        print(10)
    elif aa in [1,5,6]:
        print(aa)
    elif aa in [4,9]: # 패턴2
        bb=b%2
        print(aa*aa%10 if bb==0 else aa)

    else: #패턴 4
        bb=b%4
        print(aa**4%10 if bb==0 else aa**bb%10)


"""시간초과 난 풀이
# 당연하게 b가 너무 커서 시간초과 날 수 밖에..
T = int(input())
for _ in range(T):
    a,b=map(int,input().split())
    ans = a**b%10
    print(ans if ans else 10)
"""