a = [input() for _ in range(5)]
result = ''
max_len = max(a[::1], key=len)
for i in range(5):
    if len(a[i]) < len(max_len):
        a[i] += ' '*(len(max_len) - len(a[i]))

for i in range(len(max_len)):
    for j in range(5):
        if a[j][i] != ' ':
            result += a[j][i]
print(result)
