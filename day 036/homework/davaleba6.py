def power_2(a):
    new_list=[]
    if type(a) == list:
        for i in a:
            b = i ** 2
            new_list.append(b)
    return(new_list)

print(power_2([1, 5, 4, 8, 6, 7]))