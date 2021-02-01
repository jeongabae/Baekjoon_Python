list = []
for _ in range(9):
    list.append(int(input()))

print(max(list))
for i in range(len(list)):
    if list[i] == max(list):
        print(i)
