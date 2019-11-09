# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
final_sum = 0
for number in range(1,101):
    final_sum += number
print('The sum of all numbers from 1 to 100 is: {%d}' % final_sum)