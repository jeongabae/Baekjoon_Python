N = list(input())
N.sort(reverse=True)
print(''.join(N))
"""다른사람풀이
print(*sorted(input())[::-1],sep='')
"""
"""다른사람풀이
print(''.join(sorted(input())[::-1]))
"""
"""다른사람풀이
print("".join(sorted(input(), reverse=True)))
"""