# Make a program that reads something from the keyboard and shows its primitive type
# and all possible information about it

var1 = input('Input something: ')

if var1.isdigit():
    print('Type: ', type(int(var1)))
else:
    print('Type: ', type(var1))

print('More detais:')

if var1.isspace():
    print('Contains space')

if var1.capitalize():
    print('Is Capitalize')

if var1.isupper():
    print('Is Upper')

if var1.islower():
    print('Is Lower')
