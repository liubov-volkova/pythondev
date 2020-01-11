from datetime import datetime
import os
import psutil


#######################################################################################################################
# DECORATORS
#######################################################################################################################


# Decorator (time spent on the function execution)
def get_execution_time(f):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        f(*args, **kwargs)
        stop = datetime.now()
        print("Total time of the function execution was {}\n".format(stop - start))

    return wrapper


# Decorator (the whole process memory usage)
def get_process_memory(f):
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        memory_start = process.memory_info().rss / 100000
        f(*args, **kwargs)
        memory_finish = process.memory_info().rss / 100000
        memory_usage = memory_finish - memory_start
        if memory_usage < 0:
            memory_usage = memory_start - memory_finish
        print("Total memory usage of the function '{}' was {}".format(f.__name__, memory_usage))

    return wrapper


#######################################################################################################################
# FUNCTIONS
#######################################################################################################################


'''
    Function print a list using list's append function
    :param first_number: the minimum number
    :param last_number: the maximum number
'''


@get_execution_time
@get_process_memory
def print_number_list_v1(first_number=1, last_number=1000000):
    numbers = []
    for i in range(first_number, last_number + 1):
        numbers.append(i)
    print("Type: {}".format(type(numbers)))
    print(len(numbers))


'''
    Function print a list using iterator
    :param first_number: the minimum number
    :param last_number: the maximum number
'''


@get_execution_time
@get_process_memory
def print_number_list_v2(first_number=1, last_number=1000000):
    numbers = [i for i in range(first_number, last_number + 1)]
    print("Type: {}".format(type(numbers)))
    print(len(numbers))


'''
    Function generate a generator of numbers from first_number to last_number
    (items: integers from 1 to 1000000 by default)
    :param first_number: the minimum number
    :param last_number: the maximum number
'''


def number_generator(first_number=1, last_number=1000000):
    for i in range(first_number, last_number + 1):
        yield i


'''
    Function print a list using generator for its creating
    :param first_number: the minimum number
    :param last_number: the maximum number
'''


@get_execution_time
@get_process_memory
def print_number_list_v3(first_number=1, last_number=1000000):
    generator = number_generator(first_number, last_number)
    numbers = [next(generator) for i in range(first_number, last_number + 1)]
    print(len(numbers))


'''
    Function create a list using iterator
    (an item list: integers from 1 to 1000000 by default)
    :param first_number: the minimum number
    :param last_number: the maximum number
'''


def get_number_list(first_number=1, last_number=1000000):
    numbers = [i for i in range(first_number, last_number + 1)]
    return numbers


def print_title(title):
    dev = 80 * "*"
    print(dev)
    print(title)
    print(dev)


#######################################################################################################################
# TASK 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
# TASK 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией
#######################################################################################################################


print_title("Decorators usage:")

fn = 1
ln = 1000000
# the first version
print("The first function version:")
print_number_list_v1(fn, ln)

# the second version
print("The second function version:")
print_number_list_v2(fn, ln)

# the third version (with generator)
print("The third function version:")
print_number_list_v3(fn, ln)


#######################################################################################################################
# TASK 2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
#######################################################################################################################
print_title("Comparing of the functions execution time:")

t2_time1 = datetime.now()
num_list1 = get_number_list(fn, ln)
t2_time2 = datetime.now()
num_gen = number_generator(fn, ln)
t2_time3 = datetime.now()
time_for_list = t2_time2 - t2_time1
time_for_gen = t2_time3 - t2_time2
time_res = time_for_list > time_for_gen
if time_res:
    print("time_for_list > time_for_gen ({} difference)\n".format(time_for_list - time_for_gen))
else:
    print("time_for_list <= time_for_gen ({} difference)\n".format(time_for_gen - time_for_list))

#######################################################################################################################
# TASK 4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами:
# натуральные числа от 1 до 1000000
#######################################################################################################################

print_title("Comparing of the functions memory usage:")

process = psutil.Process(os.getpid())
memory_1 = process.memory_info().rss / 100000
num_list1 = get_number_list(fn, ln)
memory_2 = process.memory_info().rss / 100000
num_gen = number_generator(fn, ln)
memory_3 = process.memory_info().rss / 100000
memory_usage_list = memory_2 - memory_1
memory_usage_gen = memory_3 - memory_2
memory_res = memory_usage_list > memory_usage_gen

if memory_res:
    print("memory_usage_list > memory_usage_gen ({} difference)\n".format(memory_usage_list - memory_usage_gen))
else:
    print("memory_usage_list <= memory_usage_gen ({} difference)\n".format(memory_usage_gen-memory_usage_list))