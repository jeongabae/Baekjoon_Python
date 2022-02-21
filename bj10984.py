T = int(input())
for i in range(T):
    N = int(input())
    CT=GT=0
    for j in range(N):
        C, G = map(float, input().split())
        CT+=C
        GT+=C*G
    print("%d %.1f" %(CT, GT/CT))

""" 다른 분 풀이 (출력 부분 보기)
t=int(input())
for j in range(t):
    n=int(input())
    sum_a=0
    sum_b=0
    for i in range(n):
        a,b=map(float,input().split())
        sum_a += a
        sum_b += a*b

    print(int(sum_a),round(sum_b/sum_a,1))

"""