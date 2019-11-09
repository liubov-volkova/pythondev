# Найти количество цифр 5 в числе
repeat = True
fife_count = 0
while repeat:
    number = input('Enter number. I return you how many 5 figures it includes\nYour number: ')
    if number.isdigit():
        for dig in number:
            if int(dig) == 5:
                fife_count +=1
        repeat = False
    else:
        print('\nWrong input. You must enter a number! Try it again!\n')
print('This number includes {0:*^d} figures 5'.format(fife_count))