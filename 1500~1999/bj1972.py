# M = int(input())
# N = int(input())
# psn = [] #perfect square number
# i = 1
# while i**2<=N:
#     if M<=i**2 and i**2<=N:
#         psn.append(i**2)
#     i+=1
# if psn != []:
#     print(sum(psn))
#     print(psn[0])
# else:
#     print(-1)
#
#방법2
# M=int(input())
# N=int(input())
# r=[i*i for i in range(101)if M<=i*i<=N] #i는 0부터 100까지
# print("%d\n%d"%(sum(r),r[0])if r else"-1")
M=int(input())
N=int(input())
psn=[i*i for i in range(101)if M<=i*i<=N] #i는 0부터 100까지
if psn:
    print(sum(psn))
    print(psn[0])
else:
    print(-1)
