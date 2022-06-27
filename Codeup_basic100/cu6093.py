n = int(input())
a = reversed(list(map(int,input().split())))
print(*a)

"""이게 모범답안. 이것도 내 답안보다 시간 길다.
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

예시
...
for i in range(n-1, -1, -1) :
  print(a[i], end=' ')
...

참고
번호를 부른 순서를 리스트에 순서대로 기록해 두었다가, 기록한 값들을 거꾸로 출력하면 된다.
range(시작, 끝, 증감) #시작 수는 포함, 끝 수는 포함하지 않음. [시작, 끝)
range(n-1, -1, -1) #n-1, n-2, ..., 3, 2, 1, 0

"""