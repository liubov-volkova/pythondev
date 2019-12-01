from hw5pack import divisor_master as dvrs
#######################################################################################################################
# Task 1. 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
#######################################################################################################################
print(dvrs.is_simple(7))
print(dvrs.is_simple(8))

#######################################################################################################################
# Task 2. выводит список всех делителей числа
#######################################################################################################################
dvrs.print_dividers(34)

#######################################################################################################################
# Task 3. выводит самый большой простой делитель числа
#######################################################################################################################
print(dvrs.max_simple_divider(34))

#######################################################################################################################
# Task 4. функция выводит каноническое разложение числа
#######################################################################################################################
print(dvrs.get_canonical_form(34))
#######################################################################################################################
# Task 5. функция выводит самый большой делитель (не обязательно простой) числа
#######################################################################################################################
print(dvrs.max_divider(34))