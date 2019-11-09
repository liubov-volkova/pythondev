# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран
final_mlt = 1
for number in range(1,11):
    final_mlt = final_mlt * number
    print('multiplication of {:*^d} numbers is {:*^d}'.format(number,final_mlt))
print('\nThe multiplication of all numbers from 1 to 10 is: {:d}'.format(final_mlt))