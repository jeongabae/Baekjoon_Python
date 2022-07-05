import sys
T = int(sys.stdin.readline())
for _ in range(T):
  s=list(sys.stdin.readline().split())
  rev = []
  for word in s:
    rev.append(word[::-1])
  print(*rev)
"""다른사람풀이 시간 더 빠름
import sys

N = int(sys.stdin.readline())

for i in range(N):
  sentence = sys.stdin.readline()[::-1]
  store = sentence.split()
  store.reverse()
  sentence_reverse = ' '.join(store)
  print(sentence_reverse)
"""
