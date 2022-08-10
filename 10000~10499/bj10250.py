T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    Y = N % H
    XX = N//H + 1
    if Y==0:
        Y = H
        XX = N//H #원래 XX=N//H+1이라했으므로 여기서 XX-=1해도 됨
    print(Y*100+XX)
