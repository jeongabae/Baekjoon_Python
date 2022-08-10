""" 백준 1568번 : 새
브론즈2
"""
N=int(input())
i=1
ans=0
while N!=0:
    if N>=i:
        N-=i
        i+=1
        ans+=1
    else:
        i=1
print(ans)
"""아님 요렇게해도 답( if문 차이만 뒀음 )
N=int(input())
i=1
ans=0
while N!=0:
    if N<i:
        i=1
    N-=i
    i+=1
    ans+=1
print(ans)
"""