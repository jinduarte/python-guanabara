# Make a program that reads two numbers and shows the sum between them

var1 = input('Input a value: ')
var2 = input('Input other value: ')
valuesOk = True

if var1.isdigit():
    number1 = int(var1)
else:
    valuesOk = False

if var2.isdigit():
    number2 = int(var2)
else:
    valuesOk = False

if valuesOk:
    sum = number1 + number2
    print('The sum between {} and {} is equal the {}!'.format(number1, number2, sum))
else:
    print('It was not possible to show the sum')
