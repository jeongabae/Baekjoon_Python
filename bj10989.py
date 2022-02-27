# N = int(input())
# a = sorted(int(input()) for i in range(N))
# for i in a:
#     print(i)
"""메모리초과 코드
import sys
N = int(sys.stdin.readline())
a = sorted(int(sys.stdin.readline()) for i in range(N))
for i in a:
    sys.stdout.write(str(i)+'\n')
"""
import sys
n = int(sys.stdin.readline())
a = [0] * 10001
for _ in range(n):
    a[int(sys.stdin.readline())] += 1
for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i) #sys.stdout.write(str(i)+"\n")이것도 사용가능
"""
for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
일반적으로 입력값이 크지않은 경우에는 상관없지만 이렇게 입력값이 극한으로 많이 주어질 때에는
메모리를 좀 더 효율적으로 관리해야한다.
그래서 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다.
그러나 인덱스는 0부터 세기 때문에 이를 계산하기 편하게 길이가 10001인 리스트를 만든다.
"""