class Mystring:

    def __init__(self, word: str):
        self._word = word

    @property
    def word(self):
        return self.word

    def print_string(self):
        return self._word.upper()
