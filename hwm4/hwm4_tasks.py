##############################################################################################
# Task 1. Light
# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины
# N случайных имен из первого списка (могут повторяться, можно взять значения:
# количество имен 20, N = 100, рекомендуется
##############################################################################################

def get_random_items(item_list=[], n=100):
    import random
    """

    :param item_list: list if items
    :param n: amount of the random values which will be fetched
    :return: a list of the n randomly fetched items from items_list or np.nan (numpy) if items_list = Nan
    """
    rnd_items_list = []
    if len(item_list) == 0:
        return rnd_items_list
    else:
        rng = range(n)
        random_range = len(item_list) - 1
        for i in rng:
            random_ix = random.randint(0, random_range)
            rnd_items_list.append(item_list[random_ix])
        return rnd_items_list


# test 1. empty items_list and n
print('test for np.nan: ', get_random_items())
# test 2. not empty items_list, without n
test_list = ['first', 'second', 'third', 'fourth', 'fifth']
print('test for item_list: ', get_random_items(test_list))
# test 3. not empty items_list and n
test_list_3 = get_random_items(test_list, 7)
print('test for item_list: ', test_list_3)


##############################################################################################
# Task 2. Light
# Напишите функцию вывода самого частого имени из списка на выходе функции F
##############################################################################################
def get_most_often_item(items=[]):
    """

    :param items: item list to find out the most frequently occurred
    :return: one object from the item list
    """

    if len(items) == 0:
        return 'Not existed'
    from collections import Counter
    item_counter = Counter(items)
    most_popular = item_counter.most_common(1)
    return most_popular[0][0]


item = get_most_often_item(test_list_3)
print('the most frequently occurred item is: ', item)

##############################################################################################
# Task 3. Light
# Напишите функцию вывода самой редкой буквы,
# с которого начинаются имена в списке на выходе функции F
##############################################################################################
def get_most_rare_letter(items=[]):
    """

    :param items: item list to find out the most rarely occurred
    :return: one object from the item list
    """

    from operator import itemgetter
    if len(items) == 0:
        return 'Not existed'
    else:
        # get all first letters list
        first_letters_list = list(map(lambda x: x[0], items))

        # get the unique letters set
        first_letters_set = set(first_letters_list)

        # counts for each unique letter
        pairs = list(map(lambda x: (x, first_letters_list.count(x)), first_letters_set))
        sorted_pairs = sorted(pairs, key=itemgetter(1), reverse=False)
        print('General statistics: ', sorted_pairs)
        pair_min = sorted_pairs[0]
        return pair_min


min_counts_letter = get_most_rare_letter( get_random_items(test_list, 200))
print('The word with minimum counts: ', min_counts_letter)

##############################################################################################
# Task. PRO
# В файле с логами
# https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
# найти дату самого позднего лога (по метке времени).
##############################################################################################

with open('log', 'r') as f:
    from datetime import datetime
    lines = f.readlines()
    # get all strings with date time
    all_date_times = list(map(lambda l: l.split(',')[0], lines))
    # sort all dates from the nearest to the latest
    all_date_times.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M:%S'), reverse=True)
    print('All date times which are sorted:\n', all_date_times)
    print('The latest log line is: ', all_date_times[len(all_date_times)-1])
    print('The most recent log line is: ', all_date_times[0])