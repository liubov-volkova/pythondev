# Найти сумму цифр числа
repeat = True
number_sum = 0
while repeat:
    number = input('Enter number. I return you a list of its figures\nYour number: ')
    if number.isdigit():
        for dig in number:
            number_sum += int(dig)
        repeat = False
    else:
        print('\nWrong input. You must enter a number! Try it again!\n')
print('The sum of the all figures is {0:*^d}'.format(number_sum))
