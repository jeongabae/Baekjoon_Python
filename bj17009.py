a=sum([int(input())*i for i in range(3,0,-1)])
b=sum([int(input())*i for i in range(3,0,-1)])
if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('T')