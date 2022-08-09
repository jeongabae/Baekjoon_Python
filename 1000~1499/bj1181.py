n = int(input())
s = sorted(set(input() for _ in range(n)))
s.sort(key=len)
for i in s:
    print(s)
# 이 문제 마지막 두 줄을 print("\n".join(s))로 바꿀 수 있다!
"""다른 사람 풀이
import sys

num_of_words = int(sys.stdin.readline())
words = set()

for _ in range(num_of_words):
	words.add(sys.stdin.readline())

words = list(words)	
words.sort()
words.sort(key = len)

print(''.join(words))
"""