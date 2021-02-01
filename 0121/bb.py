import random as random

# ai가 고를(추론할) 숫자들 담아 놓기
num = []
for i in range(123, 9877):
    str = "%04d" % i
    if len(set(str)) == 4:
        num.append(str)


# ai가 처음 픽한 숫자
def get_ai_pick():
    ai_num = '%04d' % random.randint(123, 9877)
    while len(set(ai_num)) < 4:
        ai_num = '%04d' % random.randint(123, 9877)
    print('(Ai) 나님 숫자 골랐음 ㅋ!\n\n')
    return ai_num


# 입력 올바르면 True
def is_input_vaild(str):
    if len(str) != 4 or not str.isdecimal() or len(set(str)) != 4:
        print("Wrong Input!")
        return False
    return True


# 내 픽
def get_my_pick():
    my_num = input("생각한 4자리 숫자를 입력해주세요(중복X) : ")
    while not is_input_vaild(my_num):
        my_num = input("생각한 4자리 숫자를 입력해주세요(중복X) : ")
    return my_num


# ai 예상
def get_ai_guess_num():
    return random.choice(num)


# 내 예상
def get_my_guess_num():
    guess = input('AI가 고른 숫자가 무엇일지 추리해보세요 : ')
    while not is_input_vaild(guess):
        guess = input('AI가 고른 숫자가 무엇일지 추리해보세요 : ')
    return guess


# ai 경우의 수 지우기
def remove_case():
    remove = []
    for word in num:
        s_1, b_1 = determine(word, ai_guess)
        if s != s_1 or b != b_1:
            remove.append(word)
    for rword in remove:
        if rword in num:
            num.remove(rword)
        else:
            pass

    # num.remove(ai_guess)

    if s == 0 and b == 0:
        # print('case1')
        for word in num:
            for i in ai_guess:
                if word.find(i) != -1:
                    remove.append(word)
        for rword in remove:
            if rword in num:
                num.remove(rword)
            else:
                pass
    elif s != 4 and (s+b == 4):
        # print('case2')
        for word in num:
            if word.find(ai_guess[0]) != -1 and word.find(ai_guess[1]) != -1 and word.find(ai_guess[2]) != -1 and word.find(ai_guess[3]) != -1:
                pass
            else:
                remove.append(word)
        for rword in remove:
            if rword in num:
                num.remove(rword)
            else:
                pass

    elif s == 3:
        # print('case4')
        for word in num:
            if (word.find(ai_guess[0]) == 0 and word.find(ai_guess[1]) == 1 and word.find(ai_guess[2]) == 2) or (word.find(ai_guess[0]) == 0 and word.find(ai_guess[1]) == 1 and word.find(ai_guess[3]) == 3) or (word.find(ai_guess[0]) == 0 and word.find(ai_guess[2]) == 2 and word.find(ai_guess[3]) == 3) or (word.find(ai_guess[1]) == 1 and word.find(ai_guess[2]) == 2 and word.find(ai_guess[3]) == 3):
                pass
            else:
                remove.append(word)
        for rword in remove:
            if rword in num:
                num.remove(rword)
            else:
                pass
    elif s == 2:
        # print('case6')
        for word in num:
            c = 0
            for i in range(4):
                if word.find(ai_guess[i]) == i:
                    c += 1
            if c == 2:
                pass
            else:
                remove.append(word)
            for rword in remove:
                if rword in num:
                    num.remove(rword)
                else:
                    pass
    elif s == 1:
        # print('case3')
        for word in num:
            if word.find(ai_guess[0]) != 0 and word.find(ai_guess[1]) != 1 and word.find(ai_guess[2]) != 2 and word.find(ai_guess[3]) != 3:
                remove.append(word)
        for rword in remove:
            if rword in num:
                num.remove(rword)
            else:
                pass
    elif s + b == 3:
        # print('case5')
        for word in num:
            c = 0
            for i in ai_guess:
                if word.find(i) > -1:
                    c += 1
            if c == 3:
                pass
            else:
                remove.append(word)
            for rword in remove:
                if rword in num:
                    num.remove(rword)
                else:
                    pass
    elif s == 0:
        for word in num:
            c = 0
            for i in ai_guess:
                if word.find(i) == -1:
                    c += 1
            if c == 4:
                remove.append(word)
            else:
                pass
        for rword in remove:
            if rword in num:
                num.remove(rword)
            else:
                pass


# strike Ball 판정.
def determine(num, guess):
    strike, ball = 0, 0
    for i in range(len(num)):
        if num[i] == guess[i]:
            strike += 1
        for j in range(len(guess)):
            if num[i] == guess[j] and i != j:
                ball += 1
    return strike, ball


print('=============================')
print('MADE IN GABAE WORLD HAHAHAHA!!')
print('=============================')
my_num = get_my_pick()
ai_num = get_ai_pick()
cnt = 0
s, b = 0, 0
print('>>>>>>>>>>>>>>> Fight!!! You vs AI <<<<<<<<<<<<<<<')

while s < 4:
    if cnt % 2:
        ai_guess = get_ai_guess_num()
        print('(Ai) You가 Think한 숫자.... maybe ?->>>', ai_guess, '?')
        s, b = determine(my_num, ai_guess)
        print('%d Strike %d Ball' % (s, b))

        print('♥ ______________________________________________♥\n')
        # if s < 4:
            # print('(Ai) 아니넹 ㅋ 틀릴 수도 있지 뭐~\n\n')
        # print('ai_guess', ai_guess)
        if not s == 4:
            remove_case()
        # print(num)
    else:
        print('\n♥ ______________________________________________♥')
        my_guess = get_my_guess_num()
        s, b = determine(ai_num, my_guess)
        print('%d Strike %d Ball\n' % (s, b))
        if s == 4:
            print('(나) 내가 이겨버려쬬?!?!?! 넌 졌구용?!!?!? 역시 난 천~재~얌 ㅎ')
        # else:
        #     print('(나) 아쉽다.....\n\n')

    cnt += 1
print('\n(Ai) 아잉 내가 봐주면서 했는데... 너 되게 못한다....ㅠㅠ')
print('(Ai) 다음엔 이기도록 해봐~')
