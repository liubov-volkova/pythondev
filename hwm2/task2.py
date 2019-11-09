# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5
print('You need enter 10 figures and after that I calculate sum of all figures 5. Do your best!')
repeat = True
fife_count = 0
i = 1;
while repeat:
    str_digit = input('Enter {%d} digital: ' % i)
    if str_digit.isdigit() & len(str_digit) == 1:
        dig = int(str_digit)
        i +=1
        if dig == 5:
            fife_count+=dig
        if i == 11:
            repeat = False
    else:
        print('\nWrong input. You must enter only digital figures. Try your last input again\n')
print("You've done! The sum of all 5 among 10 figures is {%d}" % fife_count)