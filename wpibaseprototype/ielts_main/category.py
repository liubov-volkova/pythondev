import uuid
from ielts_main.value_error_castom import ValueErrorLength
from ielts_main.value_error_castom import ValueErrorType
from ielts_main.value_error_castom import ValueErrorExists


class Category:

    def __init__(self, name, max_words):
        if type(name) == str:
            if len(name) >= 3:
                if (type(max_words) == int) & (max_words > 0):
                    self.id = str(uuid.uuid4())
                    self.name = name
                    self.words = []
                    self.max_words = max_words
                else:
                    raise ValueError()
            else:
                raise ValueErrorLength()
        else:
            raise ValueErrorType()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if type(new_name) == str:
            if len(new_name) >= 3:
                self.name = new_name
            else:
                raise ValueErrorLength()
        else:
            raise ValueErrorType()

    def get_word_count_max(self):
        return self.max_words

    def get_words_left(self):
        return self.max_words - len(self.words)

    def get_words_count(self):
        return len(self.words)

    def __check_word_exists(self, word):
        found_words = [i for i in self.words if i.id == word.id]
        if len(found_words) > 0:
            return True
        else:
            return False

    def add_word(self, word):
        if self.__check_word_exists(word):
            raise ValueErrorExists
        else:
            self.words.append(word)

    def get_word_list(self):
        return [i.text for i in self.words]
