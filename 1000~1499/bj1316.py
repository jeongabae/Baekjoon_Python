N = int(input())
for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j]!=word[j+1] and word[j] in word[j+2:]:
            N-=1
            break
print(N)
"""좋은 풀이
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
    #  sorted(word, key=word.find)" 알파벳을 찾은 순으로 전부 배열한 리스트
    # word=’aabbiiaaac’일 때,
    # sorted(word,key=word.find)=’aaaaabbiic’
    # sorted(word)=’aaaaabbciii’
    # 따라서 그룹단어가 아니면 if문이 충족될 수 가 없음
    #설명 출처 : https://velog.io/@csy9604/python-%EC%BD%94%ED%85%8C-%EC%A4%80%EB%B9%84-%EA%B8%B0%EB%B3%B8-%EB%B3%B5%EC%8A%B5-3#1316-%EA%B7%B8%EB%A3%B9%EB%8B%A8%EC%96%B4%EC%B2%B4%EC%BB%A4
        result += 1
print(result)
"""
"""다른 사람코드
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)
"""