"""내풀이1
S = input()
n = [-1]*26 #알파벳이 총 26개이므로
for i in range(len(S)):
    if n[ord(S[i])-ord("a")] == -1:
        n[ord(S[i])-ord("a")] = i
print(*n)
"""
"""1등분 풀이
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')
"""
"""다른분풀이
print(*map(input().find,map(chr,range(97,123))))
"""
# S = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위
# for x in alphabet:
#     print(S.find(chr(x)),end=" ")
