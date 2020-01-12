from datetime import datetime


class ValueErrorWithExtraInfo(ValueError):
    def __init__(self, extra_info=""):
        super().__init__()
        self.extra_info = extra_info
        self.time = datetime.now()

    def set_extra_info(self, extra_info=""):
        if extra_info != "":
            self.extra_info = extra_info
