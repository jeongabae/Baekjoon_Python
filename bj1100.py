#이문제에서 0,0이 흰색. 그리고 번갈아서 색이 칠해져있으므로 x,y의 합이 2의배수이면 흰색칸, 아니라면 검정칸

board= [list(map(str,input())) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and board[i][j]=='F':
            cnt+=1
print(cnt)

"""다른분 코드 : 와 이것도 대박! 번갈아서 칠해지는거 고려해서 '0'을 더했네..
r = ''
for _ in range(8):
    r += input() + '0'
print(r[::2].count('F'))
"""
