import uuid


def check_is_str(name, error_text):
    if type(name) != str:
        raise ValueError(error_text)


def check_is_long_enaugh(name, length, error_text):
    if len(name) < length:
        raise ValueError(error_text)


class Category:

    def __init__(self, name):
        check_is_str(name, 'Category name must have a type of string.')
        check_is_long_enaugh(name, 3, 'Category name must have at least three characters.')
        self.id = uuid.uuid4()
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        check_is_str(new_name, 'Category name must have a type of string.')
        check_is_long_enaugh(new_name, 3, 'Category name must have at least three characters.')
        self.name = new_name
