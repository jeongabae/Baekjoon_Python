"""내풀이1
S = list(input())
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = [0 for i in range(26)]
for i in S:
    for j in range(26):
        if i == alphabet[j]:
            n[j] += 1
print(*n)
"""
"""다른 사람 풀이
import sys
a=[0 for i in range(26)]
s=sys.stdin.readline().strip()
for i in s:a[ord(i)-ord('a')] += 1
for i in a:print(i,end=' ')
"""
"""다른사람풀이2
a=[0]*26
for x in input():a[ord(x)-97]+=1
print(*a)
"""
#내풀이2
S = input()
n = [0]*26 #알파벳이 총 26개이므로
for i in S:
    n[ord(i)-97] += 1 #97대신 ord("a")써도 됨(<-이거 쓰는게 더 빠르게 나왔음) a의 유니코드 숫자는 97.
print(*n)
