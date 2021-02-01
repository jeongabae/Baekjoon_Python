def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i-1] == 0:
                pass
            else:
                j[i-1] = 0
                stack.append(j[i-1])
                break
        while True:
            if len(stack) > 1 and stack[-1] == stack[-2]:
                answer += 2
                stack.pop(-1)
                stack.pop(-1)
            else:
                break
    return answer
