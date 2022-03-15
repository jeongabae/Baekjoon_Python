n = int(input())
cute = 0
not_cute = 0
for i in range(n):
    if int(input()) == 1:
        cute += 1
    else:
        not_cute += 1
if not_cute > cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
