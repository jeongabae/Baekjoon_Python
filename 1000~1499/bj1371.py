import sys

s = sys.stdin.read() #입력 한 번에 다 받기 위해서 사용
li = [0]*26
for c in s:
    if c.islower():
        li[ord(c)-97] += 1
for i in range(26):
    if li[i] == max(li):
        print(chr(97+i), end='')