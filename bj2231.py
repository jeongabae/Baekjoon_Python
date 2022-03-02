#내거 중에 좋았던 풀이

def d(x):
    new_n = x
    while x != 0:
        new_n += x % 10
        x //= 10
    return new_n

n = int(input())
for i in range(1, n+1):
    if d(i)==n:
        print(i)
        break
    if i==n:
        print(0)

"""내풀이1
def d(x):
    new_n = x
    while x != 0:
        new_n += x % 10
        x //= 10
    return new_n

n = int(input())
s = []
for i in range(1, n):
    a = d(i)
    if a==n:
        s.append(i)
print(min(s) if s else 0)
"""

"""내풀이3 시간 왜 오래걸릴까?
n = int(input())

for i in range(1, n+1):
    i_sum = i
    for j in str(i):
        i_sum += int(j)
    if i_sum == n:
        print(i)
        break
    if i == n:
        print(0)
"""
"""다른 분 풀이
n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)
"""