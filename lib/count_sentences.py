#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value[-1] == ".":
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        punctuation = ".?!"

        count = 0
        start_index = 0

        for i, char in enumerate(self.value):
            if char in punctuation:
                if i == len(self.value) - 1 or self.value[i + 1] not in punctuation:
                    count += 1

        return count
