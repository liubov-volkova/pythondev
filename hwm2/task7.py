# Найти произведение цифр числа
repeat = True
number_mlt = 1
while repeat:
    number = input('Enter number. I return you a multiplication of its figures\nYour number: ')
    if number.isdigit():
        for dig in number:
            number_mlt = number_mlt * int(dig)
        repeat = False
    else:
        print('\nWrong input. You must enter a number! Try it again!\n')
print('The multiplication of the all figures is {0:*^d}'.format(number_mlt))