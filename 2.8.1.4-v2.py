def read_int(prompt, min, max):
    valoreok = False
    while not valoreok:
        try:
            value = int(input(prompt))
            valoreok = True
        except ValueError:
            print("Error: wrong input")
        if valoreok:
            valoreok = value >= min and value <= max
        if not valoreok:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return value;


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)