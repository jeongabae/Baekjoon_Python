n = int(input())
# for i in range(n):
#     for j in range(n):
#         if(i%2!=0):
#             print(" *",end="")
#         else:
#             print("* ",end="")
#     print()
#짧은건 밑의 방식인듯.
for i in range(n):
    if(i%2==0):
        print("* "*n)
    else:
        print(" *"*n)
