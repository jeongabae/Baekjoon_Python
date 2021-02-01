import copy

def renew_board(board,new):
    for i in range(len(board)):
        board[i]=new[i]


def draw_board(board):
    for i in board:
        print(" ".join(i))


def row_find(board,word):
    tempboard[0]=copy.deepcopy(board)
    tempboard[1]=copy.deepcopy(board)
    for i in range(len(board)):
        for anword in word:
            if board[i].find(anword)+1:
                idx=board[i].find(anword)
                word_dict[anword]='O'
                for j in range(len(anword)):
                    tempboard[0][i]=list(tempboard[0][i])
                    tempboard[0][i][idx+j]='■'
                    tempboard[0][i]="".join(tempboard[0][i])
            if board[i].find("".join(reversed(anword)))+1:
                idx=board[i].find("".join(reversed(anword)))
                word_dict["".join(reversed(anword))]='O'
                for j in range(len(anword)):
                    tempboard[1][i]=list(tempboard[1][i])
                    tempboard[1][i][idx+j]='■'
                    tempboard[1][i]="".join(tempboard[1][i])


def column_find(board,word):
    column=["".join(col) for col in zip(*board)]
    tempboard[2]=copy.deepcopy(column)
    tempboard[3]=copy.deepcopy(column)

    for i in range(len(column)):
        for anword in word:
            if column[i].find(anword)+1:
                idx=column[i].find(anword)
                word_dict[anword]='O'
                for j in range(len(anword)):
                    tempboard[2][i]=list(tempboard[2][i])
                    tempboard[2][i][idx+j]='■'
                    tempboard[2][i]="".join(tempboard[2][i])
            if column[i].find("".join(reversed(anword)))+1:
                idx=column[i].find("".join(reversed(anword)))
                word_dict["".join(reversed(anword))]='O'
                for j in range(len(anword)):
                    tempboard[3][i]=list(tempboard[3][i])
                    tempboard[3][i][idx+j]='■'
                    tempboard[3][i]="".join(tempboard[3][i])

    tempboard[2]=["".join(column) for column in zip(*tempboard[2])]
    tempboard[3]=["".join(column) for column in zip(*tempboard[3])]


def cross_find(board,word):#누더기 코드
    cross=[]
    for i in range(len(board)):
        board[i]=' '*i+board[i]+' '*(len(board)-i)
    for i in zip(*board):
        cross.append(list(i))
    for i in cross:
        for anword in word:
            if "".join(i).find(anword)+1:
                idx="".join(i).find(anword)
                word_dict[anword]='O'
                for j in range(len(anword)):
                    cross[cross.index(list(i))][idx+j]='■'
    for i in zip(*cross):
        tempboard[4].append("".join(i).strip())
    #반대워드
    cross=[]
    for i in zip(*board):
        cross.append(list(i))
    for i in cross:
        for anword in word:
            if "".join(i).find("".join(reversed(anword)))+1:
                idx="".join(i).find("".join(reversed(anword)))
                word_dict["".join(reversed(anword))]='O'
                for j in range(len(anword)):
                    cross[cross.index(list(i))][idx+j]='■'

    for i in zip(*cross):
        tempboard[5].append("".join(i).strip())

    #반대방향 대각선
    cross=[]
    for i in range(len(board)):
        board[i]=board[i].strip()
        board[i]=' '*i+"".join(reversed(board[i]))+' '*(len(board)-i)
    for i in zip(*board):
        cross.append(list(i))
    for i in cross:
        for anword in word:
            if "".join(i).find(anword)+1:
                idx="".join(i).find(anword)
                word_dict[anword]='O'
                for j in range(len(anword)):
                    cross[cross.index(list(i))][idx+j]='■'
    for i in zip(*cross):
        tempboard[6].append("".join("".join(reversed(i))).strip())
    #반대방향 대각선의 반대워드
    cross=[]
    for i in zip(*board):
        cross.append(list(i))
    for i in cross:
        for anword in word:
            if "".join(i).find("".join(reversed(anword)))+1:
                idx="".join(i).find("".join(reversed(anword)))
                word_dict["".join(reversed(anword))]='O'
                for j in range(len(anword)):
                    cross[cross.index(list(i))][idx+j]='■'
    for i in zip(*cross):
        tempboard[7].append("".join("".join(reversed(i))).strip())

board=[]
word=[]
tempboard=[[] for i in range(8)]
word_dict={}
#첫 번째 과제
f=open("board.txt",'r')#보드 파일 입출력으로 받아오기
while True:
    line=f.readline()
    if not line:break
    board.append("".join(line.split()))
f.close()


f=open("words.txt",'r')#워드 파일 입출력으로 받아오기
while True:
    line=f.readline().rstrip()
    if not line:break
    word.append(line)
    word_dict[line]='X'
    word_dict["".join(reversed(line))]='X'
f.close()

row_find(board,word)
column_find(board,word)
cross_find(board,word)
for i in range(len(tempboard)):
    for j in range(len(tempboard[0])):
        for k in range(len(tempboard[0][j])):
            if tempboard[i][j][k]=='■':
                tempboard[0][j]=list(tempboard[0][j])
                tempboard[0][j][k]=tempboard[i][j][k]
                tempboard[0][j]="".join(tempboard[0][j])
for i in tempboard[0]:
    for j in i:
        print(j,end=' ')
    print()
f=open("first.txt",'w')
count=0
for word,answer in word_dict.items():
    count+=1
    data=word+" "+answer
    if count%2==1:
        f.write(data+'\n')
    else:
        f.write(data+'\n\n')
f.close()

#초기화
board=[]
word=[]
tempboard=[[] for i in range(8)]
word_dict={}

#두 번째 과제
f=open("board2.txt",'r') #보드 파일 입출력으로 받아오기
while True:
    line=f.readline()
    if not line:break
    board.append("".join(line.split()))
f.close()


f=open("words2.txt",'r')#워드 파일 입출력으로 받아오기
while True:
    line=f.readline().rstrip()
    if not line:break
    word.append(line)
    word_dict[line]='X'
    word_dict["".join(reversed(line))]='X'
f.close()

row_find(board,word)
column_find(board,word)
cross_find(board,word)
for i in range(len(tempboard)):
    for j in range(len(tempboard[0])):
        for k in range(len(tempboard[0][j])):
            if tempboard[i][j][k]=='■':
                tempboard[0][j]=list(tempboard[0][j])
                tempboard[0][j][k]=tempboard[i][j][k]
                tempboard[0][j]="".join(tempboard[0][j])
for i in tempboard[0]:
    for j in i:
        print(j,end=' ')
    print()
f=open("second.txt",'w')
count=0
for word,answer in word_dict.items():
    count+=1
    data=word+" "+answer
    if count%2==1:
        f.write(data+'\n')
    else:
        f.write(data+'\n\n')
f.close()
#초기화
board=[]
word=[]
tempboard=[[] for i in range(8)]
word_dict={}
#3번째 과제
f=open("board3.txt",'r')#보드 파일 입출력으로 받아오기
while True:
    line=f.readline()
    if not line:break
    board.append("".join(line.split()))
f.close()


f=open("words3.txt",'r')#워드 파일 입출력으로 받아오기
while True:
    line=f.readline().rstrip()
    if not line:break
    word.append(line)
    word_dict[line]='X'
    word_dict["".join(reversed(line))]='X'
f.close()

row_find(board,word)
column_find(board,word)
cross_find(board,word)
for i in range(len(tempboard)):
    for j in range(len(tempboard[0])):
        for k in range(len(tempboard[0][j])):
            if tempboard[i][j][k]=='■':
                tempboard[0][j]=list(tempboard[0][j])
                tempboard[0][j][k]=tempboard[i][j][k]
                tempboard[0][j]="".join(tempboard[0][j])
for i in tempboard[0]:
    for j in i:
        print(j,end=' ')
    print()
f=open("Third.txt",'w')
count=0
for word,answer in word_dict.items():
    count+=1
    data=word+" "+answer
    if count%2==1:
        f.write(data+'\n')
    else:
        f.write(data+'\n\n')
f.close()
