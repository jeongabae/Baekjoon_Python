# 조합 사용하여 풀이했음.
# 이 문제에서 m>=n이므로 nCm이 아닌 mCn = m!/n!(m-n)!해주면 됨!
import sys
import math
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n)) #조합 mCn 사용
    print(bridge)

"""이건 DP(Dynamic Programming) 쓴 다른 분 풀이
dp[num][pick] = dp[num-1][pick] + dp[num-1][pick-1]보다 나는 조합 공식 쓰는 풀이가 바로 생각났음.
이 풀이랑 비슷한 풀이(거의 똑같은 풀이) 설명은 -> 설명이 잘 되어 있는 블로그 https://honggom.tistory.com/142 참고!
import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1

for num in range(1,31):
    dp[num][0] = 1
    for pick in range(1,31):        
        dp[num][pick] = dp[num-1][pick] + dp[num-1][pick-1]

for _ in range(T):
    N, M = map(int,input().split())
    print(dp[M][N])"""