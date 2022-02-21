T = int(input())
if T % 10:
    print(-1)
else:
    print(T // 300, (T % 300) // 60, (T % 60) // 10)



# T=int(input())
# if T%10!=0:
#     print(-1)
# else:
#     A=T//300
#     T%=300
#     B=T//60
#     T%=60
#     C=T//10
#     print(A,B,C)
"""
T = int(input())
A = T // 300
T %= 300
B = T // 60
T %= 60
C = T // 10
print(-1) if T%10!=0 else print(A,B,C)
"""
'''1등 코
T = int(input())
print(*[[T // 300, T // 60 % 5, T // 10 % 6], [-1]][T % 10 > 0])
'''