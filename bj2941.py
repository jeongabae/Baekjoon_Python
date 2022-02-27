"""내풀이1
c = ["c=","c-", "dz=", "d-", "lj", "nj", "s=","z="]
n = input()
cnt = len(n)
for i in c:
    cnt -= n.count(i)
print(cnt)
"""
#내풀이2
c = ["c=","c-", "dz=", "d-", "lj", "nj", "s=","z="]
n = input()
print(len(n)-sum(n.count(i) for i in c))
"""
다른분풀이
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))
"""
