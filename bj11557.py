T = int(input())
for i in range(T):
    N = int(input())
    univ = dict()
    for j in range(N):
        S, L = map(str, input().split())
        univ[int(L)] = S
    print(univ[max(univ.keys())])

    """1등 답
    for i in range(int(input())):
        high = 0
        highschool = 0  # lol
        for j in range(int(input())):
            school, amount = input().split()
            if int(amount) > high:
                highschool = school
                high = int(amount)
        print(highschool)
   """
