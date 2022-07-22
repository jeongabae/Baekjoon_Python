N=int(input())
print("SK" if N%2 else "CY")
"""
1일 때는 SK 승

2일 때는 CY 승

3일 때는 SK 승

4일 때는 CY 승
...
"""

""" 동적계획법(DP)(Dynamic Programming)을 이용한 풀이
import sys
def input():
    return sys.stdin.readline().rstrip()

dp = ['' for _ in range(1001)]
dp[1] = 'SK'

for i in range(1,1000):
    if dp[i]=="SK":
        if dp[i+1]=='':
            dp[i+1] = 'CY'
        if i+3<1000:
            dp[i+3] = 'CY'
    elif dp[i]=='CY':
        if dp[i+1]=='':
            dp[i+1] = 'SK'
        if i+3<1000:
            dp[i+3] = 'SK'

print(dp[int(input())])
"""