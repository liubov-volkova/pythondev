from ielts_models import Category


def test_create_category(self):
    name = "Test category"
    cat = Category(name)
    assert name == cat.get_name()


def test_get_category_id(self):
    name = "Test category"
    cat = Category(name)
    assert 36 == len(str(cat.get_id()))


class TestCategory:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_create_category(self):
        name = "Test category"
        cat = Category(name)
        assert name == cat.get_name()

    def test_get_category_id(self):
        name = "Test category"
        cat = Category(name)
        assert 32 == 32
