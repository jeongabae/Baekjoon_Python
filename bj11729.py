n = int(input())
def hanoi(n, source, desti, mid):
    if n == 1:
        print(source, desti) # 원판이 하나인 경우 source(1)-> desti(3)으로 옮기면 끝!
    else:
        hanoi(n - 1, source, mid, desti)# 원판 n-1개를 source(1)에서 mid(2)로 옮긴다. desti(3)을 보조 기둥으로 사용.
        print(source, desti)            # 제일 밑에 있는 원판(n번째 원반)을 desti(3)로 이동.
        hanoi(n - 1, mid, desti, source) # mid(2)에 있는 원반 n-1개를 desti)3)로 이동. source(1)을 보조 기둥으로 사용.
print(2**n -1) # 이동 총 개수는 2^n -  1이다.
hanoi(n, 1, 3, 2)