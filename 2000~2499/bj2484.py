import sys
def input():
    return sys.stdin.readline().rstrip()

def money():
    dice = sorted(list(map(int, input().split())))
    if len(set(dice)) == 1:
        return dice[0] * 5000 + 50000
    if len(set(dice)) == 2:
        if dice[1] == dice[2]:
            return dice[1] * 1000 + 10000
        else:
            return (dice[1] + dice[2]) * 500 + 2000
    for i in range(3):
        if dice[i] == dice[i+1]:
            return dice[i] * 100 + 1000
    return dice[-1] * 100

N = int(input())
result = [money() for i in range(N)]
print(max(result))

"""1등 분 코드
import sys
input = sys.stdin.readline
def func(lst):
    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + lst[0] * 500 + lst[2] * 500
    for i in range(3):
        if lst[i] == lst[i+1]:
            return 1000 + lst[i] * 100
    return lst[3] * 100

N = int(input())
max_lst = []
for _ in range(N):
    lst = sorted(list(map(int, input().split())))
    max_lst.append(func(lst))
print(max(max_lst))
"""