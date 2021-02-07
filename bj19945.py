n = int(input())
print(32if n < 0 else len(bin(n))-2)
# 2를 빼주는 이유 0b101010 이런식으로 나와서...!
