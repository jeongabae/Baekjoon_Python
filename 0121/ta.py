
import random

possible_list=[]

for possible in range(123,10000):
    if possible<1000 and len(set(str(possible)))==3 and '0' not in str(possible):
        possible_list.append('0'+str(possible))
    if len(set(str(possible)))==4:
            possible_list.append(str(possible))


def is_digit(user_input_number):
    try:
        for i in user_input_number:
            num=int(i)
        return True
    except:
        return False

def is_between_0123_and_9876(user_input_number):
    if len(user_input)>4:
        return False
    for i in user_input_number:
        if(0 > int(i) and int(i) > 9):
            return False
    return True



def is_duplicated_number(four_digit):
    if(len(set(four_digit))==4):
        return False
    else:
        return True


def is_validated_number(user_input_number):
    if(is_digit(user_input_number) and is_between_0123_and_9876(user_input_number) and not is_duplicated_number(user_input_number)):
        return True
    else:
        return False



def get_strikes_or_ball(user_input_number, answer):
    result = [0,0]
    for i in range(4):
        if str(user_input_number[i])==answer[i]:
            result[0]+=1
        elif str(user_input_number[i]) in answer:
            result[1]+=1
    return result


def is_yes(one_more_input):
    if(one_more_input.upper() == 'YES' or one_more_input.upper() == 'Y'):
        return True
    else:
        return False


def is_no(one_more_input):
    if(one_more_input.upper() == 'NO' or one_more_input.upper() == 'N'):
        return True
    else:
        return False


def ai(ai_clue,player_answer,possible_list):
    sb=get_strikes_or_ball(ai_clue,player_answer)
    removelist=[]
    if sb[0]==0 and sb[1]==0:
        for possible in possible_list:
            count=0
            for number in ai_clue:
                if number in list(possible):
                    count+=1
            if count!=0:
                removelist.append(possible)
    for possible in possible_list:
        strike_same=0
        ball_same=0
        for i in range(len(possible)):
            if (possible[i]==ai_clue[i]):
                strike_same+=1
            elif possible[i] in ai_clue:
                ball_same+=1
        if strike_same!=sb[0] or ball_same!=sb[1]:
            removelist.append(possible)
    for mustremove in set(removelist):
        possible_list.remove(mustremove)


print("Play Baseball")
user_input = list(str(9999))
play=True
stat=0

ai_answer=10000
# ===Modify codes below=============
while user_input!='0':
    while not is_validated_number(ai_answer):
        ai_answer=str(random.randrange(123,10000))
    answer= input("당신의 숫자 4글자를 입력하세요 : ")
    while not is_validated_number(answer):
        print("잘못된 입력입니다")
        answer= input("당신의 숫자 4글자를 입력하세요 : ")
    while True:
        print()
        user_input = input("상대방의 숫자를 예상해보세요 : ")
        if is_validated_number(user_input):
            print("Strikes :",get_strikes_or_ball(user_input,ai_answer)[0], ", Balls :",get_strikes_or_ball(user_input,ai_answer)[1])
        elif user_input=='0':
            break
        else:
            print("잘못된 입력입니다")
            continue
        if get_strikes_or_ball(user_input,ai_answer)==[4,0]:
            print("플레이어의 승리!")
            break
        ai_clue=possible_list[0]
        print()
        print("Ai도 예상했습니다. Ai의 예상은 ",ai_clue)
        print("Ai Strikes:",get_strikes_or_ball(ai_clue,answer)[0],",Ai Balls:",get_strikes_or_ball(ai_clue,answer)[1])
        ai(ai_clue,answer,possible_list)
        if get_strikes_or_ball(ai_clue,answer)==[4,0]:
            print("Ai의 승리!\n")
            break

    if(user_input!='0'):
        check=True
    else:
        check=False
    while check:
        pos=input("게임이 끝났습니다, 다시 하시겠습니까?(Y/N) ?")
        if is_no(pos):
            check=False
            stat+=1
            break
        elif is_yes(pos):
            play=True
            check=False
        else:
            print("잘못된 입력입니다")
    if stat==1:
        break

print("=============끝==============")
