time = sum([int(input()) for _ in range(4)])
m,s = divmod(time,60) #몫과 나머지가 동시에 나오는 문제는 divmod(대상,나눌 수)
print(m)
print(s)