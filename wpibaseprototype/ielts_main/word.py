import uuid
from ielts_main.value_error_castom import ValueErrorLength
from ielts_main.value_error_castom import ValueErrorType


class Word:
    def __init__(self, category_id, text, description):
        if type(category_id) == str:
            if len(category_id) == 36:
                self.id = uuid.uuid4()
                self.categoryId = category_id
                self.text = text
                self.description = description
            else:
                raise ValueErrorLength()
        else:
            raise ValueErrorType()