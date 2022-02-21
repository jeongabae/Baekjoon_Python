T = int(input())
for i in range(T):
    n = int(input())
    bi = list(bin(n))
    bi.reverse()
    for j in range(len(bi)):
        if bi[j]=="1": print(j,end=" ")
"""다른사람풀이1
T = int(input())
for _ in range(T):
    B = f'{int(input()):2b}'[::-1]
    G = (b for b in range(len(B)) if B[b] == '1')
    print(*G)
"""

"""다른사람풀이2
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = format(int(input()), 'b')
    print(*(i for i, x in enumerate(reversed(a)) if int(x)))
"""