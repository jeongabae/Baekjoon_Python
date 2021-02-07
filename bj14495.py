# n = int(input())
# f = [1, 1, 1, 1] #f[0]은 없으니...그냥 1이라고 함..!
# for i in range(4, n+1):
#     f.append(f[i-1] + f[i-3])
# print(f[n])

f = [0, 1, 1] #f[0]은 없으니...그냥 1이라고 함..!
for i in range(117):
    f.append(f[-1] + f[-3])
print(f[int(input())])
