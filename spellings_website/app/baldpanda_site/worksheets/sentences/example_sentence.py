from random import shuffle
from baldpanda_site.worksheets.blanked_words.word_with_blanks import WordWithBlanks

class ExampleSentence:
    """Sentence object with methods able to maninpulate it with"""

    def __init__(self, line):
        self.sentence = line

    def remove_space_before_punct(self, list_of_punct):
        """Remove single space before any punctation in list within
        sentence
        """
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(" " + punct, punct)
        return sentence

    def add_space_before_punct(self, list_of_punct):
        """Add single space before any punctation in list within
        sentence
        """
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(punct, " " + punct)
        return sentence

    def add_space_before_and_after_punct(self, list_of_punct):
        """Add single space before and after any punctation in list
         within sentence
        """
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(punct, " " + punct + " ")
        return sentence

    def remove_space_before_and_after_punct(self, list_of_punct):
        """Remove single space before and after any punctation in list
         within sentence
        """
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(" " + punct + " ", punct)
        return sentence

    def sentence_normaliser(self):
        """returns list of lowercase words contained in sentence"""
        sent_norm = self.sentence.replace("\n", "")
        sent_norm = sent_norm.split(" ")
        sent_norm = [word.lower() for word in sent_norm]
        return sent_norm

    def blank_out_word_in_sentence(self, word):
        """blanks out word from within sentence"""
        self.sentence = self.add_space_before_and_after_punct([",", ".", "!", "?", '"'])
        sentence_list = self.sentence.split(" ")
        sent_list_norm = self.sentence_normaliser()
        word_loc = sent_list_norm.index(word.lower())
        if "'" in word:
            apost_loc = word.split("'")
            sentence_list[word_loc] = WordWithBlanks(apost_loc[0]).replace_all_letters_with_blanks()\
            + "'" + WordWithBlanks(apost_loc[1]).replace_all_letters_with_blanks()
        else:
            sentence_list[word_loc] = WordWithBlanks(word).replace_all_letters_with_blanks()
        updated_sentence = " ".join(sentence_list)
        self.sentence = updated_sentence
        self.sentence = self.remove_space_before_and_after_punct([",", ".", "!", "?", '"'])
        return self.sentence

    def generate_mult_sentences_with_blanks(self, list_of_words):
        shuffle(list_of_words)
        all_example_sentences = ""
        for word in list_of_words:
            ex_sentence = ExampleSentence("")
            all_example_sentences += ex_sentence.blank_out_word_in_sentence(word) + "\n"
        return all_example_sentences
