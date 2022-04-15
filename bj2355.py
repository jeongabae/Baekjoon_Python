"""시간초과가 난 코
import sys
a,b=map(int,sys.stdin.readline().split())
print(sum(i for i in range(a,b+1)))드
"""
"""다른분 코드1
import sys
n,m=map(int,sys.stdin.readline().split())
max_ = max(n, m)
min_ = min(n, m)
d = max_ - min_
sum = (d * (d + 1))//2
print(sum + min_ * (d + 1))
"""
#다른분 코드2
"""
범위가 매우 넓기 때문에 단순 for문으로 계산을 시도하면 시간초과 혹은 메모리초과가 발생하게 된다.

따라서 O(1)만에 문제를 해결할 수 있는 가우스의 공식을 활용한다.

 

1부터 n까지의 합은 (n+1) * n // 2 라고 표현할 수 있다.

하지만, 이 문제는 1부터의 합이 아닌 a부터 b까지의 합이다.

따라서, 1부터 b까지의 합과 1부터 a-1까지의 합의 차를 출력한다.

단, a < b로 고정하기 위해 a가 b보다 크면 두 수를 교체해준다.
"""
a,b = map(int,input().split())
if a>b:
    a,b=b,a
print(b*(b+1)//2-a*(a-1)//2)