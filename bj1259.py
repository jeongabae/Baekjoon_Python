while 1:
    n = input()
    if n=='0': break
    n_re = n[::-1]
    print("yes" if n==n_re else "no")
"""다른 분 코드 : 내꺼랑 결이 비슷하심. 
x = input()
while x != '0':
    print("yes" if x == x[::-1] else "no")
    x = input()
"""