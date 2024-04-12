class IllegalCQCodeError(BaseException):
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return f'{self.text}不是合法的CQ码'