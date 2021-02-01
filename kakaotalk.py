chat = []
f = open('/Users/jeongabae/workspace/kakao/KakaoTalk_20210112_0314_25_973_group.txt', 'r', encoding='utf-8')
while True:
    tmp = f.readline()
    if tmp == '':
        break
    chat.append(tmp.strip())
f.close()

# 스터디 멤버List
member = ['김태훈', '백승민', '신희승', '이용빈', '이한진', '전가배', '정건',
          '정연재', '정현진', '현승민']
# 멤버별 대화량
conversations_number = {i: 0 for i in member}
# 멤버별 이모티콘 전송량
emoticon_frequency = {i: 0 for i in member}
# 멤버별 사진 전송량
pictures_frequency = {i: 0 for i in member}
# 멤버별 대화 삭제량
delete_frequency = {i: 0 for i in member}
# 날짜별 대화수
date_conversations = {}
# 시간대별 대화수
time_conversations = {i: 0 for i in range(24)}
# 단어 등장수
word_frequency = {}

# --------------------- 위 코드는 만지지 말아주세요. 각 dict와 list가 초기화되어있습니다.
# 아래 print 코드는 chat과 dict에 어떤 데이터가 들어가있는지 확인해보시고
# 지우시면 됩니다.
# print(*chat, sep='\n')
for line in chat:
    words = line.split()
    if not (line[0] == '-' or line[0] == '['):
        continue

    if line[0] == '-':
        date = "-".join(words[1:5])
        date_conversations[date] = 0
    date_conversations[date] += 1
    if line[0] == '[':
        name = words[0][1:-1]
        time = words[1:3]
        message = words[3:]
        conversations_number[''.join(name)] += 1

        for i in message:
            if i in word_frequency:
                word_frequency[i] += 1
            else:
                word_frequency[i] = 1

        if ''.join(message) == '이모티콘':
            emoticon_frequency[''.join(name)] += 1
        if ''.join(message) == '사진':
            pictures_frequency[''.join(name)] += 1
        if ''.join(message) == '삭제된메시지입니다.':
            delete_frequency[''.join(name)] += 1

        if '[오후' in time:
            time = int(time[1][0:time[1].find(':')]) + 12
        else:
            time = int(time[1][0:time[1].find(':')])
        if time == 24:
            time = 0
        time_conversations[time] += 1
print("========== 대화 수 ==========")
f = open("/Users/jeongabae/workspace/kakao/conversation_number.txt", 'w')
conversation_number = dict(sorted(conversations_number.items(), reverse=True, key=lambda item: item[1]))
for key, value in conversation_number.items():
    print(key, value)
    f.write(key+"\t"+str(value)+"\n")
print()
f.close()

print("========== 이모티콘 수 ==========")
f = open("/Users/jeongabae/workspace/kakao/emoticon_frequency.txt", 'w')
emoticon_frequency = dict(sorted(emoticon_frequency.items(), reverse=True, key=lambda item: item[1]))
for key, value in emoticon_frequency.items():
    print(key, value)
    f.write(key+"\t"+str(value)+"\n")
print()
f.close()

print("========== 사진 수 ==========")
f = open("/Users/jeongabae/workspace/kakao/pictures_frequency.txt", 'w')
pictures_frequency = dict(sorted(pictures_frequency.items(), reverse=True, key=lambda item: item[1]))
for key, value in pictures_frequency.items():
    print(key, value)
    f.write(key+"\t"+str(value)+"\n")
print()
f.close()

print("========== 삭제 수 ==========")
f = open("/Users/jeongabae/workspace/kakao/delete_frequency.txt", 'w')
delete_frequency = dict(sorted(delete_frequency.items(), reverse=True, key=lambda item: item[1]))
for key, value in delete_frequency.items():
    print(key, value)
    f.write(key+"\t"+str(value)+"\n")

print()
f.close()

print("========== 날짜별 ==========")
f = open("/Users/jeongabae/workspace/kakao/date_conversations.txt", 'w')
for key, value in date_conversations.items():
    print(key, value)
    f.write(key+"\t"+str(value)+"\n")
print()
f.close()

print("========== 시간대 별 ==========")
f = open("/Users/jeongabae/workspace/kakao/time_conversations.txt", 'w')
for key, value in time_conversations.items():
    print(key, value)
    f.write(str(key)+"\t"+str(value)+"\n")
print()
f.close()

f = open("/Users/jeongabae/workspace/kakao/word_frequency.txt", 'w')
word_frequency = dict(sorted(word_frequency.items(), reverse=True, key=lambda item: item[1]))
for key, value in word_frequency.items():
    f.write(key+"\t"+str(value)+"\n")
f.close()
