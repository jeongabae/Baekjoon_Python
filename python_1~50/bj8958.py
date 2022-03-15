n = int(input())

for _ in range(n):
    ox_list = list(input())
    correct = 0
    sum = 0
    for ox in ox_list:
        if ox == 'O':
            correct += 1
            sum += correct
        else:
            correct = 0
    print(sum)
