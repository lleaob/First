def power(x, y):
    rsl = 1
    for i in range(y):
        rsl *= x
    return(rsl)

base_num = int(input("Type base number: "))
pow_num = int(input("Type power number: "))

print(power(base_num, pow_num))