#정렬, 구현
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a[-k])