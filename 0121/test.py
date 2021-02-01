num = []
for i in range(123, 1234):
    str = "%04d" % i
    if len(set(str)) == 4:
        num.append(str)

# print(num[0][0])
sb = [1, 0]
remove = []
ai_guess = '1234'
# print(num[0].find(ai_guess[0]))
if sb[0] == 1:
    for word in num:
        print('word', word, 'idx', word.find(ai_guess[0]))
        print('word', word, 'idx', word.find(ai_guess[1]))
        print('word', word, 'idx', word.find(ai_guess[2]))
        print('word', word, 'idx', word.find(ai_guess[3]))
        if word.find(ai_guess[0]) != 0 and word.find(ai_guess[1]) != 1 and word.find(ai_guess[2]) != 2 and word.find(ai_guess[3]) != 3:
        # for i in range(4):
            # if word.find(ai_guess[i]) != i:
            if word in num:
                print('remove : ', word)
                remove.append(word)
    for rword in remove:
        num.remove(rword)
print(num)
# for word in num:
#     print(word)
