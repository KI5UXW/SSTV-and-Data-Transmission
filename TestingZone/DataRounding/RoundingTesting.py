def dataConversion(number):
    if number < 10 and number > 0:
        number = round(number, 2)
        number = "+" + str(number)
    elif number < 100 and number > 0:
        number = round(number, 1)
        number = "+" + str(number)
    elif number < 1000 and number > 0:
        number = round(number, 0)
        number = "+" + str(number)
    elif number > -10 and number < 0:
        number = round(number, 2)
        number = str(number)
    elif number > -100 and number < 0:
        number = round(number, 1)
        number = str(number)
    elif number > -1000 and number < 0:
        number = round(number, 0)
        number = str(number)
    else:
        number = str(number)
        print("Number outside of bounds.")
    return number

print(str(dataConversion(-1.122134345)))
print(str(dataConversion(100.222312)))
print(str(dataConversion(10)))
print(str(dataConversion(-10)))
print(str(dataConversion(-654.22232)))
print(str(dataConversion(1.234)))
print(str(dataConversion(10000)))