def esPrimo(n):
    #divisible entre 1 o el mismo
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        #11 / 2
        #11 / 3
        #11 / ...
        #11 / 10
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
for i in range(-10, 101):
    print(i, "", esPrimo(i))

"""y si se quiere preguntar por un numero especifico: """

print(esPrimo(367))