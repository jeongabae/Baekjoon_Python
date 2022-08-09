x = int(input())
line = end =  0
while x > end:
    line += 1
    end += line #해당 라인에 제일 끝 인덱스(만약 n이 5이면 line 3이고 그 라인의 끝 번호는 6이므로 end는 6이다.

diff = end - x #끝 번호와 x(n)번째의 차이
if line%2 == 0: #짝수 라인일 때
    top = line - diff
    bottom = diff + 1
else: #홀수 라인일 때    top = diff + 1
    bottom = line - diff
print(f"{top}/{bottom}")
#print("%d/%d"%(top,bottom)) 이것도 됨
"""
1번째 라인에 분수 1개 2번째 라인에 분수 2개,...,i번째 라인에 분수 i
짝수번째 라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소

홀수번째 라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 증가.
"""

"""다른 분 코드
X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line-X+1
else:
    a = line-X+1
    b = X

print(a, '/', b, sep='')
"""