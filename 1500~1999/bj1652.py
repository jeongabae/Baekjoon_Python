n = int(input())
room = []
res_h = 0
res_w = 0
for _ in range(n):
    room.append(list(map(str,input())))

for i in range(n):
    cnt_h, cnt_w = 0,0
    for j in range(n):
        if room[i][j] == '.':
            cnt_h +=1
        elif room[i][j] == 'X':
            if cnt_h >=2:
                res_h += 1
            cnt_h = 0
        if room[j][i] == '.':
            cnt_w +=1
        elif room[j][i] == 'X':
            if cnt_w >=2:
                res_w += 1
            cnt_w = 0

        if j == n-1:
            if cnt_h >=2:
                res_h += 1
            if cnt_w >=2:
                res_w += 1

print('%d %d'%(res_h,res_w))
