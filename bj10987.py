w = input()
s = 0
for i in 'aeiou':
    s+=w.count(i)
print(s)
"""한 줄 코딩
print(sum(map(input().count,"aeiou")))
"""