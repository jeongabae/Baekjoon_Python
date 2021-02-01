import random as random


# ai 숫자 생각하기
def getAIThinkNum():
    ai_num = '9999'
    while len(set(ai_num)) < 4:
        ai_num = '%04d' % random.randint(123, 9877)
    print('(Ai) 나님 숫자 골랐음 ㅋ!\n')
    return ai_num


# 가능한 모든 함수 확인.
def getAiPossible():
    p = []
    for i in range(123, 9877):
        str = "%04d" % i
        if len(set(str)) == 4:
            p.append(str)
    return p


# 가능한 모든 함수 확인.
def getAiPossible(p):
    for i in range(123, 9877):
        str = "%04d" % i
        if len(set(str)) == 4:
            p.append(str)
    return p


# 플레이어가 생각한 숫자 가져오기
def getPlayerThinkNum():
    pl_num = input("생각한 4자리 숫자를 입력해주세요(중복X) : ")
    while not isInputVaild(pl_num):
        pl_num = input("생각한 4자리 숫자를 입력해주세요(중복X) : ")
    return pl_num


# 플레이어의 예상
def getPlayerGuessNum():
    guess = input('AI가 고른 숫자가 무엇일지 추리해보세요 : ')
    while not isInputVaild(guess):
        guess = input('AI가 고른 숫자가 무엇일지 추리해보세요 : ')
    return guess


# Ai가 생각한 숫자
def getAIGuessNum():
    return aiPossible[random.randint(0, len(aiPossible)-1)]


# 입력이 올바른지 확인
def isInputVaild(str):
    # 문자열 길이가 4가 아니거나, int형으로 변환 불가능하거나, 중복된 수 있으면
    if len(str) != 4 or not str.isdecimal() or len(set(str)) != 4:
        print("Wrong Input!")
        return False
    return True


# Ai가 추론해서 가능성 언ㅂㅅ앰
def aiThink(guess, sb):
    remove = []
    for case in aiPossible:
        tmp_sb = determine(case, guess)
        if sb != tmp_sb:
            remove.append(case)
    print(remove)
    for case in remove:
        aiPossible.remove(case)


# strike Ball 판정.
def determine(num, guess):
    strike, ball = 0, 0
    for i in range(len(num)):
        if num[i] == guess[i]:
            strike += 1
        for j in range(len(guess)):
            if num[i] == guess[j] and i != j:
                ball += 1
    return [strike, ball]


print('==========================')
print('!가배의 숫자야구 게임 START!')
print('==========================')
p = []
pl_num = getPlayerThinkNum()
ai_num = getAIThinkNum()
aiPossible = getAiPossible(p)
cnt = 0
sb = [0, 0]
while sb[0] < 4:
    if cnt % 2:
        ai_guess = getAIGuessNum()
        print('(Ai) 너 ->>>', ai_guess, '<<<- 이 숫자 생각했쥐?!!')
        sb = determine(pl_num, ai_guess)
        print('%d Strike %d Ball' % (sb[0], sb[1]))
        if sb[0] < 4:
            print('(Ai) 아니넹 ㅋ 틀릴 수도 있지 뭐~\n\n')
        aiThink(ai_guess, sb)
    else:
        pl_guess = getPlayerGuessNum()
        sb = determine(ai_num, pl_guess)
        print('%d Strike %d Ball' % (sb[0], sb[1]))
        # if sb[1] == 4:
        #     print('(나) 내가 이겨버려쬬?!?!?! 넌 졌구용?!!?!? 역시 난 천~재~얌 ㅎ')
        # else:
        #     print('(나) 아쉽다.....\n\n')
    cnt += 1
# print('\n(Ai) 아잉 내가 봐주면서 했는데... 너 되게 못한다....ㅠㅠ')
# print('(Ai) 다음엔 이기도록 해봐~')
