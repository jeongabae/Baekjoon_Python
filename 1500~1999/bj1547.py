M = int(input())
a = [0,1,0,0] # 원래 1이 공을 가지고 있으므로 인덱스 1만 1로 초기화
for _ in range(M):
    X, Y = map(int,input().split())
    a[X],a[Y]=a[Y],a[X] #입력이 들어오면 그 둘을 바꿔줌.
print(a.index(1))