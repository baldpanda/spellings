import six_words_with_spaces

class All_words:

    def __init__(self):
        self.all_words = ""

    def generate_all_words(self, list_of_words):
        for word in list_of_words:
            six_words = six_words_with_spaces.Six_words_with_blanks()
            self.all_words += six_words.generate_six_words_with_blanks(word) + "\n"
        return self.all_words

all_words = All_words()
print(all_words.generate_all_words(["apple", "carrot"]))
