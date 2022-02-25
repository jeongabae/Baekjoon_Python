n = input()
s = 0
num = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
for i in range(len(n)):
    s += num[ord(n[i])-65]
print(s)
"""다른분풀이
alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
li = list(input())
result = 0
for i in li:
    for j in alphabet:
        if i in j:
            result += alphabet.index(j)+3
print(result)
"""
"""다른 분 풀이
alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0
for unit in alphabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alphabet_list.index(unit) +3  # time = time + index +3
print(time)
"""