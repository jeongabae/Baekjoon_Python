while 1:
    n = int(input())
    if n==0:
        break
    sieve = [False, False] + [True] * (2*n - 1)  # 0과 1은 소수가 아님 #2부터는 일단 True라고 해놓고 for문에서 나머지 해결!
    cnt = 0
    for i in range(2, 2 * n + 1): #이건 나누는 수!
        if sieve[i]:
            for j in range(2 * i, 2 * n + 1, i):  # 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.(false로...)
                sieve[j] = False
            if i>n:
                cnt += 1
    print(cnt)
"""시간 초과 
while 1:
    n = int(input())
    if n==0:
        break
    cnt = 0
    for i in range(n+1,2*n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j ==0:
                break
        else:
            cnt += 1
    print(cnt)
"""