T = int(input())
for i in range(T):
    n, word = input().split()
    word = list(word)
    word.pop(int(n)-1)
    print("".join(word))