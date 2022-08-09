"""계속 시간초과난 코드
N = input()
fir = N
cnt = 0
while 1:
    if len(N)==1:
        N = "0"+N
    plus = str(int(N[0])+int(N[1]))
    N = N[-1]+ plus[-1]
    cnt += 1
    if N == fir:
        print(cnt)
        break
"""
N = int(input())
fir = N
cnt = 0
while 1:
    left = N//10
    right = N%10
    new_right = (left+right)%10
    N = (right*10)+new_right
    cnt += 1
    if N == fir:
        print(cnt)
        break