# N, K = map(int, input().split())
# a = []
# for i in range(N,0,-1):
#     if(N%i==0):
#         a.append(N // i)
# print(a[K-1] if K<=len(a) else 0)

N, K = map(int, input().split())
a = [i for i in range(1, N+1) if N%i==0]
print(0 if len(a)<K else a[K-1])
'''
if K>len(a):
    print(0)
else:
    print(a[K-1])
'''