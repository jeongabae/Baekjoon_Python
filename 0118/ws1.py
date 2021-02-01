def printBoard():
    print(*[' '.join(resultBoard[i]) for i in range(MAX_Y)], sep='\n')


def finding(line, r_line):
    for word in words.keys():
        if word.upper() in line:
            words[word] = 'O'
            r_line = r_line.replace(word, '■'*len(word))
    return r_line


def find_row():
    line = [''.join(board[i]) for i in range(MAX_Y)]
    r_line = [''.join(resultBoard[i]) for i in range(MAX_Y)]
    for i in range(MAX_Y):
        # line = ''.join(board[i])
        # r_line = ''.join(resultBoard[i])
        r_line = finding(line, r_line)
        resultBoard[i] = list(r_line)


def find_colomn():
    for i in range(MAX_X):

        line = ''
        r_line = ''
        for j in range(MAX_Y):
            line += board[j][i]
            r_line += resultBoard[j][i]

        r_line = finding(line, r_line)

        for j in range(MAX_Y):
            resultBoard[j][i] = r_line[j]


def find_left_diagnol():
    for _ in range(MAX_X+MAX_Y-1):

        line = ''
        r_line = ''
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i+j == _:
                    line += board[i][j]
                    r_line += resultBoard[i][j]

        r_line = finding(line, r_line)

        cnt = 0
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i+j == _:
                    resultBoard[i][j] = r_line[cnt]
                    cnt += 1


def find_right_diagnol():
    for _ in range(MAX_X+MAX_Y-1):

        line = ''
        r_line = ''
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i-j+(MAX_X-1) == _:
                    line += board[i][j]
                    r_line += resultBoard[i][j]

        r_line = finding(line, r_line)

        cnt = 0
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i-j+(MAX_X-1) == _:
                    resultBoard[i][j] = r_line[cnt]
                    cnt += 1


# board.txt 읽어와서 board 리스트 만들기.
f = open('board.txt', 'r')
board = f.read().split('\n')
for i in range(len(board)):
    board[i] = board[i].split()
f.close()

MAX_X = len(board[0])
MAX_Y = len(board)

# 출력할 board
resultBoard = [[chr for chr in str] for str in board]

# words.txt파일 읽어와서 words 리스트 만들기.
f = open('words.txt', 'r')
words = {}
for word in f.read().split():
    words[word] = 'X'
    words[word[::-1]] = 'X'
f.close()

find_row()
find_colomn()
find_left_diagnol()
find_right_diagnol()

printBoard()
cnt = 0
for k, v in words.items():
    if not cnt % 2:
        print()
    print(k, v)
    cnt += 1
