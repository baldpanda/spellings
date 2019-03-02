"""Generating words containing varying numbers of blanks"""
from random import sample, randint

class WordWithBlanks:
    """Word with varying number of its letters
    replaced by blanks"""
    def __init__(self, word):
        self.word = word

    def insert_blanks_in_word(self, num_blanks):
        """Inserts n blanks in a word in a random position"""
        word = self.word
        alt_word = list(word)
        leng = len(word)
        #not including apostrophe as letter that can be blanked
        if "'" in word:
            apost_loc = word.index("'")
            if num_blanks > apost_loc:
                num_blanks = apost_loc
            if randint(0, 1) == 0:
                replace_char_index = sample(range(0, apost_loc), (num_blanks))
            else:
                replace_char_index = sample(range(0, apost_loc), (num_blanks))\
                + list(range((apost_loc + 1), leng))
        else:
            replace_char_index = sample(range(0, leng), num_blanks)
        rev_replace_char_index = sorted(replace_char_index, reverse=True)
        for i in rev_replace_char_index:
            alt_word[i] = " _ "
        alt_word = "".join(alt_word)
        return alt_word

    def replace_all_letters_with_blanks(self):
        """Replaces all letters in word with blanks"""
        len_of_word = len(self.word)
        if len_of_word == 1:
            blanked_word = "_"
        else:
            blanked_word = "_"
            for i in range(0, len_of_word - 1):
                blanked_word += " _"
        return blanked_word
