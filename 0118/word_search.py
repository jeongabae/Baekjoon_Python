def isWordInLine(line, word):
    return line.find(word.upper())


def horizontal(word):
    lines = [''.join(line) for line in board]
    for i in range(MAX_Y):
        idx = isWordInLine(lines[i], word)
        if idx == -1:
            continue
        for j in range(len(word)):
            resultBoard[i][idx+j] = '♥'
        words[word] = '0'
        return True
    return False
    # for line in range(len(board)):
    #     for word in words:
    #         if word:
    #             tmp = isWordInLine(''.join(board[line]), word)
    #             if tmp != -1:
    #                 word[word] = [tmp, line, 'r']
    #             tmp = isWordInLine(''.join(board[line]), word[::-1])
    #             if tmp != -1:
    #                 words[word] = [tmp, line, 'r']


def vertical(word):
    # for i in range(len(borad[0])):
    #     line = [j][i] for j in board]
    #     for word in words:
    #         if word:
    #             tmp = isWordInLine(''.join(line))
    #         if tmp != -1:
    #             words[word] = [i, tmp, 'd']
    #         tmp = isWordInLine(''.join(line))
    #         if tmp != -1:
    #             words[word] = [i, tmp, 'd']
    lines = [''.join(line) for line in board]
    for i in range(MAX_X):
        idx = isWordInLine(lines[i], word)
        if idx == -1:
            continue
        for j in range(len(word)):
            resultBoard[idx+i][j] = '♥'
        words[word] = '0'
        return True
    return False


# 좌하향 대각선
def diagonal_p(word):
    for d in range(MAX_X+MAX_Y-1):
        line = ''
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i+j == d:
                    line += board[i][j]
        idx = isWordInLine(line, word)
        if idx == -1:
            continue
        if d < MAX_X:
            x, y = d - idx, idx
        else:
            x, y = (MAX_X - 1)-idx, d - (MAX_X-1) + idx
        for i in range(len(word)):
            resultBoard[y+i][x-i] = '♥'  # 왼쪽 화살표
        words[word] = '0'
        return True
    return False
# def diagnal_p():
#     for d in range(len(board)+len(board[0])-1):
#         line = []
#         for i in range(len(board)):


def diagonal_m(word):
    for d in range(MAX_X+MAX_Y-1):
        line = ''
        for i in range(MAX_Y):
            for j in range(MAX_X):
                if i+j == d:
                    line += board[i][j]
        idx = isWordInLine(line, word)
        if idx == -1:
            continue
        if d < MAX_X:
            x, y = (MAX_X - 1) - d + idx
        else:
            x, y = idx, d - (MAX_X-1)
        for i in range(len(word)):
            resultBoard[y+i][x-i] = '♥'  # 왼쪽 화살표
        words[word] = '0'
        return True
    return False


f = open('board.txt', 'r')
board = f.read().split('\n')
for i in range(len(board)):
    board[i] = board[i].split()
f.close()
MAX_X = len(board[0])
MAX_Y = len(board)

resultBoard = [[chr for chr in str]for str in board]

f = open('words.txt', 'r')
words = {i: 0 for i in f.read().split()}
f.close()
for word in words:
    print(word)

# for i in board:
#     print(' '.join(i))
# print('\n\n')

# horizontal()
#
# vertical()
#
# diagnal_p()
#
# diagonal_m()
# for word in words:
    # x, y, direction = words[word]
    # cord = []
    # if horizontal(word) is True:
    #     cord = [(i, y) for i in range(x, x+len(word))]
    # elif vertical(word) is True:
    #     cord = [(x, i) for i in range(y, y+len(word))]
    # elif diagonal_p(word) is True:
    #     x_ = [i for i in range(x, x-len(word), -1)]
    #     y_ = [i for i in range(y, y + len(word))]
    #     cord = list(zip(x_, y_))
    # else:
    #     x_ = [i for i in range(x, x+len(word))]
    #     y_ = [i for i in range(y, y+len(word))]
    #     cord = list(zip(x_, y_))

    # x, y, direction = words[word]
    # cord = []
    # if direction == 'd':
    #     cord = [(x, i) for i in range(y, y_len(word))]
    # elif direction == 'r':
    #     cord = [(i, y) for i in range(x, x_len(word))]
    # elif direction = 'rd':
    #     x_ = [i for i in range(x, x+len(word))]
    #     y_ = [i for i in range(y, y+len(word))]
    #     cord = list(zip(x_, y_))
    # else:
    #     x_ = [i for i in range(x, x-len(word)), -1]
    #     y_ = [i for i in range(y, y-len(word))]
    #     cord = list(zip(x_, y_))
    # for i, j in cord:
    #     board[j][i] = '♥'
    # print(word, ': (x, y) =>', (x, y), '방향 -', direction)

    # for i in board:
    #     print(' '.join(i))
