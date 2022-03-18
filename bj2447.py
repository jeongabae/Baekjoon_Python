def getStar(arr):
    result = [] #별을 담을 리스트 선언
    for i in range(len(arr) * 3): #인자로 전달된 리스트의 길이 * 3만큼 반복(별의 총 줄 개수가 3배씩 늘어나기 때문 ex)3 -> 9 -> 27 ...)
        star = arr[i % len(arr)]
        if i // len(arr) == 1: #인자로 전달된 리스트의 길이로 나눈 몫이 1일 경우(즉,별모양에서 중간에 빈칸이 들어가는 경우의 범위)
            result.append(star+ " " * len(arr) +star) #해당 빈칸의 개수만큼(인자로전달된 리스트의 길이가 빈칸의 개수)별 중간에 추가해준다.
        else:#그 외 경우
            result.append(star* 3) #리스트에 저장되어있는 별의 개수 * 3배 만큼 추가해준다.(각 줄마다 별의 개수가 3배만큼 증가하기 때문)
    return result #별이 저장되어 있는 리스트를 반환


star_pattern = ["***", "* *", "***"] # n==3일 때의 별 초기화

n = int(input())
cnt = 0 #별의 개수를 구하는 함수(get_stars) 반복횟수 구하기

while n != 3: #n이 3이아닐때 반복(3이면 그냥 바로 출력)
    n //= 3 #n을 3으로 나눈 몫을 대입
    cnt += 1 #한번 나눌때 마다 count값 1씩 증가

for _ in range(cnt): #count값 만큼 반복(n이 9이상일 때)
    star_pattern = getStar(star_pattern) #반복할 때마다 별의 개수가 줄마다 3배씩 늘어나기 때문에 늘어난 별의 개수를 그 전 개수 별의 리스트에 대입해준다.

for i in star_pattern: #리스트에 저장되어있는 별을 줄마다 출력
    print(i)