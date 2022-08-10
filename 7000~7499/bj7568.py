N = int(input())
build = []
rank = []
for i in range(N):
    x, y = map(int,input().split())
    build.append([x,y])
for j in range(N):
    cnt = 0
    for k in range(N):
        if build[j][0]<build[k][0] and build[j][1]<build[k][1]:
            cnt+=1 # 몸무게와 키 모두 자신보다 큰 사람의 수를 카운트하여 +1해준다.
    rank.append(cnt+1) #등수는 cnt보다 1크다. 예를 들어 자기보다 큰 사람이 2명있으면 나는 3등.
print(*rank)
"""다른 사람 코드 나랑 조오금 다름
num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
"""