N = int(input())
a = []
for i in range(N//5+1):
    for j in range(N//3+1):
        if i*5+j*3==N:
            a.append(i+j)
if len(a)==0:
    print(-1)
else:
    print(min(a))

"""다른 사람 풀이
n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    if b%3 == 0:
        c = b//3
        
        break
    a -= 1
    b += 5
        
if b%3 == 0:
    print(a+c)
else:
    print(-1)
"""
"""다른 사람 풀이
N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt = cnt + (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break
"""
"""다른 사람 풀이
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
 """