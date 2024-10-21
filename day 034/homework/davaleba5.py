def nums():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    num=int(input("Insert your number: "))
    if num in numbers:
        print(num)
    else:
        print("number was not found")

nums()