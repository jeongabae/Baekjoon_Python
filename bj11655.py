S = input()
result = ""
for i in S:
    if i.islower():
        result += chr((ord(i)+13-97)%26+97) #a : 97이므로 원래 소문자에서 +13번째 알파벳을해주고 -97을 해주고 26으로 나눈 나머지를 구해줘야됨.그리고 시작인 a(97)을 더해줘야 원하는 문자가 나옴
    elif i.isupper():
        result += chr((ord(i) + 13 - 65) % 26 + 65) #A : 65
    else:
        result += i
print(result)
"""1등 분 코드
for i in input():
    if i.isupper():
        t=ord(i)+13
        if t>90:
            t-=26
        print(chr(t),end='')
    elif i.islower():
        t=ord(i)+13
        if t>122:
            t-=26
        print(chr(t),end='')
    else:
        print(i,end='')
"""