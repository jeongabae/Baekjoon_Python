a = int(input())
b = int(input())
c = b - a

if c >= 31:
    print("You are speeding and your fine is $500.")
elif c > 20:
    print("You are speeding and your fine is $270.")
elif c > 0:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")