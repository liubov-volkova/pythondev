from hw5pack import divisor_master as dm


def test_is_simple_true():
    assert dm.is_simple(17) == True


def test_is_simple_false():
    assert dm.is_simple(24) == False


def test__get_dividers():
    test_list = [1, 2, 17, 34]
    assert dm._get_dividers(34) == test_list


def test__get_all_simple_dividers():
    assert dm._get_all_simple_dividers([1, 2, 4, 17, 24]) == [2, 17]


def test_max_simple_divider():
    assert dm.max_simple_divider(34) == 17
    