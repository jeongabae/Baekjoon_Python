# # pypy3로 제출해야 시간초 안남
# n = int(input())
# a = [int(input()) for i in range(n)]
# print(sum(a)-(n-1))

#방법2 (얘도 pypy로 받아야)
# n = int(input())
# a=0
# for i in range(n):
#     a+=int(input())
# print(a-(n-1))과

import sys
n=int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]
print(sum(a)-(n-1))