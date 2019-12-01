

def _get_dividers(number):
    """

    :param number: int from 1 to 1000
    :return: all dividers of this number
    """
    dividers = []
    for i in range(1, number + 1):
        if number % i == 0:
            dividers.append(i)
    return dividers


def is_simple(number):
    """

    :param number: int figure
    :return: true or false depending if it is simple or not integer figure
    """

    divrs_list = _get_dividers(number)
    if (len(divrs_list) == 2) == True & ((1 in divrs_list) == True) & ((number in divrs_list) == True):
        return True
    else:
        return False

def print_dividers(number):
    divrs_list = _get_dividers(number)
    print("all dividers' list: ", divrs_list)

def _get_all_simple_dividers(divs_list):
    """

    :param divs_list: all dividers list, integer number list
    :return: only simple divider list
    """
    simple_dvrs = []
    for i in range(0, len(divs_list)):
        if is_simple(divs_list[i]):
            simple_dvrs.append(divs_list[i])
    return simple_dvrs


def max_simple_divider(number):
    """

    :param number: integer from 1 to 10000
    :return: max simple divider of the number
    """
    divrs_list = _get_dividers(number)
    simple_dvrs = _get_all_simple_dividers(divrs_list)
    if len(simple_dvrs) == 1:
        return 1
    else:
        return max(simple_dvrs)


def max_divider(number):
    """

    :param number: integer from 1 to 10000
    :return: max divider of the number
    """
    return max(_get_dividers(number))


def _multiple(num_list):
    res = 1
    for i in range(0, len(num_list)):
        res = res * num_list[i]
    return res


def get_canonical_form(number):
    start_number = number
    simple_dvrs = _get_all_simple_dividers(number)
    print(len(simple_dvrs))
    canonical_items = []
    for i in range(len(simple_dvrs)):
        while start_number % simple_dvrs[i] == 0:
            canonical_items.append(simple_dvrs[i])
            start_number = start_number / simple_dvrs[i]

    if _multiple(canonical_items < number):
        last_num = number / _multiple(canonical_items)
        canonical_items.append(last_num)
    return canonical_items