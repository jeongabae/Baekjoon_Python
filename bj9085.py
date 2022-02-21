
T = int(input())
for i in range(T):
    N = int(input())
    print(sum(list(map(int, input().split()))))

'''
T = int(input())
result = []
for i in range(T):
    N = int(input())
    a = input().split()
    sum = 0
    for j in a:
        sum+=int(j)
    print(sum)
'''
'''
t = int(input())
answer = []
for i in range(t):
    n = int(input())
    li = input().split()
    print(li)
    sum = 0
    for j in li:
        sum+=int(j)
    answer.append(sum)

for i in answer:
    print(i)
'''
'''이것보다 위의 풀이가 쉽지만 아래의 방법도 숙지해놓을 
T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    sum = 0
    for j in range(N):
        sum += nums[j]
    print(sum)
    
'''