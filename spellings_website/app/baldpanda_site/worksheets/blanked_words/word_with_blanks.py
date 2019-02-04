from random import sample, randint
import os

data_path = os.path.join(os.getcwd(), 'sentences.txt')

class Word_with_blanks:

    def __init__(self, word):
        self.word = word

    def insert_blanks_in_word(self, num_blanks):
        word = self.word
        alt_word = list(word)
        leng = len(word)
        #keeping apostrophe in the word at all times to avoid confusion with users
        if "'" in word:
            apost_loc = word.index("'")
            if num_blanks > apost_loc:
                num_blanks = apost_loc
            if randint(0,1) == 0:
                replace_char_index = sample(range(0,apost_loc), (num_blanks))
            else:
                replace_char_index = sample(range(0,apost_loc), (num_blanks)) + list(range((apost_loc + 1),leng))
        else:
            replace_char_index = sample(range(0, leng), num_blanks)
        rev_replace_char_index = sorted(replace_char_index, reverse=True)
        for i in rev_replace_char_index:
            alt_word[i] = " _ "
        alt_word = "".join(alt_word)
        return alt_word

    def replace_all_letters_with_blanks(self):
        len_of_word = len(self.word)
        if len_of_word == 1:
            a = "_"
        else:
            a = "_"
            for i in range(0, len_of_word - 1):
                a += " _"
        return(a)
