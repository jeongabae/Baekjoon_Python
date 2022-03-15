while True:
    n = int(input())
    if n == -1:
        break
    divisor = [1]
    for i in range(2,n):
        if n%i == 0:
            divisor.append(i)
    if n == sum(divisor):
        print(n, " = ", " + ".join(str(i) for i in divisor), sep="")
    else:
        print(n, "is NOT perfect.")