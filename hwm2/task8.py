# Дать ответ на вопрос: есть ли среди цифр числа 5
repeat = True
has_fife = False
while repeat:
    number = input('Enter number. I return you if it includes 5 figure or not\nYour number: ')
    if number.isdigit():
        for dig in number:
<<<<<<< HEAD
            if int(dig) == 5:
                has_fife = True
=======
            has_fife = int(dig) == 5
>>>>>>> origin/master
        repeat = False
    else:
        print('\nWrong input. You must enter a number! Try it again!\n')
print('This number includes 5 figure: {0:*^s}'.format(str(has_fife)))
