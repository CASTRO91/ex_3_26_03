import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):

    def __init__(self, lang="Eng", letters=string.ascii_uppercase):
        super().__init__(lang, letters)
        self._letters_num = len(string.ascii_uppercase)

    def is_en_letters(self, letters):
        self.letters = letters
        return True if self.letters in string.ascii_letters else False

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        print('sample text in english:\nSome years ago — never mind how long precisely — having little or no\n'
              'money in my purse, and nothing particular to interest me on shore, I thought I would sail\n'
              'about a little and see the watery part of the world.')


obg_alpha = EngAlphabet()
print(obg_alpha.letters)
print(obg_alpha.letters_num())
print(obg_alpha.is_en_letters('F'))
print(obg_alpha.is_en_letters('Щ'))
obg_alpha.example()

