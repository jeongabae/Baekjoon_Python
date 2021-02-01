f = open('board3.txt', 'r')
board = f.read().split('\n')
for i in range(len(board)):
    board[i] = board[i].split()
f.close()
result_board = [[ch for ch in li] for li in board]
max_x, max_y = len(board[0]), len(board)

f = open('words3.txt', 'r')
words = {}
for word in f.read().split():
    words[word] = 'X'
    reverse_word = word[::-1]
    words[reverse_word] = 'X'
f.close()


def word_checking(line, result):
    for word, there_is_or_isnt in words.items():
        large_word = word.upper()
        if large_word in line:
            words[word] = 'O'
            # result = result.replaceAll(word, len(word)*'■')# 아 이거 자바...
            result = result.replace(word, len(word)*'■')
    return result


def horizontal():
    for i in range(max_y):
        lines = ''.join(board[i])
        result = list(word_checking(lines, ''.join(result_board[i])))
        result_board[i] = result


def vertical():
    for i in range(max_x):
        lines, result = '', ''
        for j in range(max_y):
            lines += board[j][i]
            result += result_board[j][i]
        result = word_checking(lines, result)

        for j in range(max_y):
            result_board[j][i] = result[j]


def diagnol_left():
    for d in range(max_x+max_y-1):
        cnt, line, result = 0, '', ''
        for y in range(max_y):
            for x in range(max_x):
                if x+y == d:
                    line += board[y][x]
                    result += result_board[y][x]
        result = word_checking(line, result)
        for y in range(max_y):
            for x in range(max_x):
                if x+y == d:
                    result_board[y][x] = result[cnt]
                    cnt += 1


def diagnol_right():
    for d in range(max_x+max_y-1):
        cnt, line, result = 0, '', ''
        for y in range(max_y):
            for x in range(max_x):
                if (max_x-1)+y-x == d:
                    line += board[y][x]
                    result += result_board[y][x]

        result = word_checking(line, result)
        for y in range(max_y):
            for x in range(max_x):
                if (max_x-1)+y-x == d:
                    result_board[y][x] = result[cnt]
                    cnt += 1


horizontal()
vertical()
diagnol_left()
diagnol_right()

f = open("4.txt", 'w')
person_distancing = 0
for i in range(max_y):
    f.write(*[' '.join(result_board[i])])
    f.write("\n")
for k, v in words.items():
    output = k+" "+v
    if person_distancing % 2 == 0:
        f.write("\n")
    f.write(output+"\n")
    person_distancing += 1
f.close()
