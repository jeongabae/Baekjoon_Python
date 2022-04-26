while 1:
    try:
        print(input())
    except EOFError:#입력이 끝남(End Of File) 에러 : 데이터가 없어 더 이상 값을 읽을 수 없을 때 발생하는 에러
        break