import sys
from collections import Counter
N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])
print(round(sum(arr)/N))
print(arr[N//2])
mode = Counter(arr).most_common(2)
if len(arr)==1:
    print(mode[0][0])
else:
    print(mode[0][0] if mode[0][1]!=mode[1][1] else mode[1][0])
print(max(arr)-min(arr))