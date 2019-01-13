import os
from random import shuffle
from baldpanda_site.word_with_blanks import Word_with_blanks

class Example_sentence:

    def __init__(self, line):
        self.sentence = line

    def remove_space_before_punct(self, list_of_punct):
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(" " + punct, punct)
        return(sentence)

    def add_space_before_punct(self, list_of_punct):
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(punct, " " + punct)
        return(sentence)

    def add_space_before_and_after_punct(self, list_of_punct):
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(punct, " " + punct + " ")
        return(sentence)

    def remove_space_before_and_after_punct(self, list_of_punct):
        sentence = self.sentence
        for punct in list_of_punct:
            sentence = sentence.replace(" " + punct + " ", punct)
        return(sentence)

    def sentence_normaliser(self):
        sent_norm = self.sentence.replace("\n", "")
        sent_norm = sent_norm.split(" ")
        sent_norm = [word.lower() for word in sent_norm]
        return(sent_norm)

    def blank_out_word_in_sentence(self, word):
        self.sentence = self.add_space_before_and_after_punct([",", ".", "!", "?", '"'])
        sentence_list = self.sentence.split(" ")
        sent_list_norm = self.sentence_normaliser()
        word_loc = sent_list_norm.index(word.lower())
        leng = len(word)
        if "'" in word:
            apost_loc = word.split("'")
            sentence_list[word_loc] = Word_with_blanks(apost_loc[0]).replace_all_letters_with_blanks()+ "'" + Word_with_blanks(apost_loc[1]).replace_all_letters_with_blanks()
        else:
            sentence_list[word_loc] = Word_with_blanks(word).replace_all_letters_with_blanks()
        updated_sentence = " ".join(sentence_list)
        self.sentence = updated_sentence
        self.sentence = self.remove_space_before_and_after_punct([",", ".", "!", "?", '"'])
        return(self.sentence)

    def generate_mult_sentences_with_blanks(self, list_of_words):
        shuffle(list_of_words)
        all_example_sentences = ""
        for word in list_of_words:
            ex_sentence = Example_sentence("")
            all_example_sentences += ex_sentence.blank_out_word_in_sentence(word) + "\n"
        return(all_example_sentences)
