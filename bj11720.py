n = int(input())
s = input()
score = []
sum = 0
for i in range(n):
    score.append(int(s[i]))
    sum += score[i]
print(sum)


# 제일 쉬운 풀이
# input()
# print(sum(map(int, input())))
