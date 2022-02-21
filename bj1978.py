N = int(input())
num = list(map(int, input().split()))
for i in num:
    if i == 1:
        N -= 1
    for j in range(2, i):
        if i % j == 0:
            N -= 1
            break
print(N)
"""짧은 다른분 풀이
input()
print(sum(all(i%j for j in range(2,i))*i>1 for i in map(int,input().split())))
"""