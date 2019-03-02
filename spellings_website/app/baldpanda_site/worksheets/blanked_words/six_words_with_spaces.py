"""Uses word with blanks to generate the same word six times with varying numbers
of letters replaced by blanks "_"
"""
from random import randint
from baldpanda_site.worksheets.blanked_words.word_with_blanks import WordWithBlanks


class SixWordsWithBlanks:
    """Object repeating the same word six times with varying numbers of
    blanks
    """
    def __init__(self):
        self.words = ""

    def generate_six_words_with_blanks(self, word):
        """"Given a word, will return the word six times with
        a varying number of blanks
        """
        word_len = len(word)
        for num_spaces in range(1, 7):
            word_containing_blanks = WordWithBlanks(word)
            if word_len - num_spaces >= 0:
                self.words += word_containing_blanks.insert_blanks_in_word(num_spaces)\
                + ", "
            else:
                self.words += word_containing_blanks.insert_blanks_in_word(randint(1, word_len))\
                + ", "
            num_spaces += 1
        return self.words[:-2]
