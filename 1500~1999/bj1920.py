n, a = input(), set(map(int, input().split()))
m = input()
x = list(map(int, input().split()))
for i in x:
    print(1 if i in a else 0)
