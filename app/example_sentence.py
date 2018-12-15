import os
from random import shuffle
import word_with_blanks as wwb
#sentences.txt is a text file containing all of the current sentences
data_path = os.path.join(os.getcwd(), 'sentences.txt')


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

    def sentence_normaliser(self):
        sent_norm = self.sentence.replace("\n", "")
        sent_norm = sent_norm.split(" ")
        sent_norm[0] = sent_norm[0].lower()
        sent_len = len(sent_norm)
        return(sent_norm)

    def search_txt_file_for_word(self, word):
        searchfile = open(data_path, "r+")
        sentence = ""
        for line in searchfile:
            ex_sentence = Example_sentence(line)
            sent_norm_list = ex_sentence.sentence_normaliser()
            poss_sent = " ".join(sent_norm_list)
            ex_sentence.sentence = poss_sent
            if word in ex_sentence.add_space_before_punct([",", ".", "!", "."]).split(" "):
                sentence = line
                ex_sentence.sentence = line
                break
        if not sentence:
            sentence = input('Please give a sentence with the word {} in: '.format(word))
            ex_sentence.sentence = sentence
            searchfile.write("\n" + sentence)
        searchfile.close()
        return(ex_sentence.sentence.strip("\n"))

    def blank_word_in_sentence(self, word):
        self.sentence = self.search_txt_file_for_word(word)
        self.sentence = self.add_space_before_punct([",", ".", "!", "?"])
        sentence_list = self.sentence.split(" ")
        sent_list_norm = self.sentence_normaliser()
        word_loc = sent_list_norm.index(word)
        leng = len(word)
        if "'" in word:
            apost_loc = word.split("'")
            sentence_list[word_loc] = wwb.Word_with_blanks(apost_loc[0]).replace_all_letters_with_blanks()+ "'" + wwb.Word_with_blanks(apost_loc[1]).replace_all_letters_with_blanks()
        else:
            sentence_list[word_loc] = wwb.Word_with_blanks(word).replace_all_letters_with_blanks()
        updated_sentence = " ".join(sentence_list)
        self.sentence = updated_sentence
        self.sentence = self.remove_space_before_punct([",", ".", "!", "?"])
        return(self.sentence)

    def generate_mult_sentences_with_blanks(self, list_of_words):
        #words need to be shuffled as list of words will be given at top of
        #document
        shuffle(list_of_words)
        all_example_sentences = ""
        for word in list_of_words:
            ex_sentence = Example_sentence("")
            all_example_sentences += ex_sentence.blank_word_in_sentence(word) + "\n"
        return(all_example_sentences)
