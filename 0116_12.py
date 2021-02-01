person, win = input().split()
batting = []
a_score, b_score = 0, 0
dividend_rate = {}
for i in range(int(person)):
    name_team_money = input().split()
    batting.append(name_team_money)
    if name_team_money[1] == 'A':
        a_score += int(name_team_money[2])
    else:
        b_score += int(name_team_money[2])

dividend_rate['A'] = (a_score+b_score)/a_score+0.005
dividend_rate['B'] = (a_score+b_score)/b_score+0.005

print('%.2f %.2f' % (dividend_rate['A'], dividend_rate['B']))

for i in batting:
    if win == i[1]:
        print('%s %.f' % (i[0], dividend_rate[win]*i[2] + 0.5))
    else:
        print(i[0], 0)
