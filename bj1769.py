x = input()
cnt = 0
while len(x) != 1:
    cnt += 1
    n = 0
    for i in x:
        n += int(i)
        x = str(n)
print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")
