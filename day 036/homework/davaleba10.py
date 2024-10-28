def only_prime(a):
    prime_list=[]
    for num in a:
            if num <= 1:
                 return None
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return None
            prime_list.append(num)
    return(prime_list)

print(only_prime([3, 4, 7, 10, 13, 18]))