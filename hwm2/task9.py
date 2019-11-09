# Найти максимальную цифру в числе
repeat = True
max_dinamyc_val = 'not defined'
all_figures = []
while repeat:
    number = input('Enter number. I return you the maximum figure in it\nYour number: ')
    if number.isdigit():
        max_dinamyc_val = int(number[0])
        for dig in number:
            figure = int(dig)
            all_figures.append(figure)
            if figure > max_dinamyc_val:
                max_dinamyc_val = figure
        repeat = False
    else:
        print('\nWrong input. You must enter a number! Try it again!\n')

print('The maximum figure is (dynamic val) {0:*^s}'.format(str(max_dinamyc_val)))
print('\nThe second way to calculate the maximum figure:')
max_figure = all_figures[0]
for i in range(len(all_figures)):
    if all_figures[i] > max_figure:
        max_figure = all_figures[i]
print('The maximum figure is (array of figures) {0:*^s}'.format(str(max_figure)))