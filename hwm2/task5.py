# Вывести цифры числа на каждой строчке
repeat = True
all_figures = []
while repeat:
    number = input('Enter number. I return you a list of its figures\nYour number: ')
    if number.isdigit():
        for dig in number:
            all_figures.append(int(dig))
        repeat = False
    else:
        print('\nWrong input. You must enter a number! Try it again!\n')
print('The figures list:')
for i in range(len(all_figures)):
    print(all_figures[i])