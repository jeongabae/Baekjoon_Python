"""내풀이1
W=[int(input()) for i in range(10)]
K=[int(input()) for i in range(10)]
W.sort(reverse=True)
K.sort(reverse=True)
print(W[0]+W[1]+W[2],end=" ")
print(K[0]+K[1]+K[2])
"""
"""내풀이2
W=[int(input()) for i in range(10)]
K=[int(input()) for i in range(10)]
W.sort()
K.sort()
print(W[7]+W[8]+W[9],end=" ")
print(K[7]+K[8]+K[9])
"""
"""내풀이3
W=[int(input()) for i in range(10)]
K=[int(input()) for i in range(10)]
W.sort()
K.sort()
print(sum(W[7:]), sum(K[7:]))
"""
W=sorted([int(input()) for i in range(10)])[7:]
K=sorted([int(input()) for i in range(10)])[7:]
print(sum(W),sum(K))