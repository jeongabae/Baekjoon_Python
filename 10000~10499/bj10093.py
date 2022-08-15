# 백준 10093번 : 숫자 : 구현
a, b = map(int, input().split())
a2, b2 = min(a, b), max(a, b)
ans = [i for i in range(a2+1, b2)]
print(len(ans))
print(*ans)
""" 더 좋은 풀이
A,B=map(int,input().split())
A,B=min(A,B),max(A,B)
print(len(range(A+1,B)))
print(' '.join(map(str,range(A+1,B))))
"""