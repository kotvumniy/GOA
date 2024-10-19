def a_or_b():
    a=int(input("Insert your number: "))
    b=int(input("Insert your number: "))
    if a > b:
        print(str(a) + " is the biggest")
    else:
        print(str(b) + " is the biggest")

a_or_b()