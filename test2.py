def powers_of_2(n):
    power = 1
    for i in range(n):
        print(i)

        print(power)
        yield power
        power *= 2
 
 
for v in powers_of_2(8):
    print(v)