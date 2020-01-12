from datetime import datetime


class ValueErrorLength(ValueError):
    def __init__(self):
        self.message = "Incorrect value length"
        self.time = datetime.now()

    def __str__(self):
        return  "{}: {}".format(self.time, self.message)


class ValueErrorType(ValueError):
    def __init__(self):
        self.message = "Incorrect value type"
        self.time = datetime.now()

    def __str__(self):
        return "{}: {}".format(self.time, self.message)


class ValueErrorExists(ValueError):
    def __init__(self):
        self.message = "The value has already existed"
        self.time = datetime.now()

    def __str__(self):
        return "{}: {}".format(self.time, self.message)


class IndexErrorOutOfRange(IndexError):
    def __init__(self):
        self.message = "The value is over the limit"
        self.time = datetime.now()

    def __str__(self):
        return "{}: {}".format(self.time, self.message)

