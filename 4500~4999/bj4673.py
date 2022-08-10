"""풀이1
n = set(range(1,10001))
have_n = set()
for i in range(1,10001): #i=123
    for j in str(i):    #j = "1","2","3"
        i+= int(j)      #123+1+2+3, i=129
    have_n.add(i)
self_n = sorted(n-have_n) #self_n type은 list(sorted를 안하면 set)
for i in self_n:
    print(i)
"""
def d(n):
    new_n = n
    while n != 0:
        new_n += n % 10
        n //= 10
    return new_n

not_self = set()
for i in range(1,10001):
    not_self.add(d(i))
for i in range(1, 10001):
    if (i not in not_self):
        print(i)
"""
#테스트 123
def d(n):
    new_n = n
    while n != 0:
        print("n:",n)
        new_n += n % 10
        print("new_n += n %% 10 : %d = %d + %d" % (new_n,n,n%10))
        n //= 10
        print("n //= 10 :", n)
    return new_n
print("d:",d(123))
"""

"""다른분풀이
def d(a):
    if (a < 10):
        return a + a
    elif (a < 100):
        return a + a // 10 + a % 10
    elif (a < 1000):
        return a + a // 100 + (a % 100) // 10 + a % 10
    else:
        return a + a // 1000 + (a % 1000) // 100 + (a % 100) // 10 + a % 10
a = set()
for i in range(10000):
    a.add(d(i))
for i in range(1, 10000):
    if (i not in a):
        print(i)
"""
"""다른분풀이 
def I(n):
  s = 0
  while n:
    s+= n % 10
    n //= 10
  return s
E=[0]*10001;
for i in range(0,10001):
  K=i+I(i);
  if(K<=10000): E[K]=1;
for i in range(0,10001):
  if E[i]==0: print(i);
"""

"""다른분풀이
isSelf = [True for i in range(11000)]

def funcD(n) :
	make = n
	while n != 0 :
		make += n%10
		n //= 10
	return make

for i in range(10000) :
	isSelf[funcD(i)] = False

for i in range(1, 10001) :
	if isSelf[i] :
		print(i)
"""