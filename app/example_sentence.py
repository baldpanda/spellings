import os
from random import shuffle
#import mult_words_blanks as mwb
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
        for a in searchfile:
            line = Example_sentence(a)
            sent_norm_list = line.sentence_normaliser()
            poss_sent = " ".join(sent_norm_list)
            if word in line.add_space_before_punct([",", ".", "!", "."]).split(" "):
                sentence = line
                break
        if not sentence:
            sentence = input('Please give a sentence with the word {} in: '.format(word))
            searchfile.write("\n" + sentence)
        searchfile.close()
        return(line.sentence.strip("\n"))


    def blank_word_in_sentence(self, word):
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

abc = Example_sentence("I have a carrot.")
print(abc.blank_word_in_sentence("have"))



def example_sentence_mult(list_of_words):
    """Takes a list of words and returns an example sentence for each.
    For each of these sentences the target word is blanked out.

    Args:
        list_of_words (list): list of the words wanted for example sentences

    Returns:
        (str): Example sentences for each word in the input, with each
        new sentence on a new line
    """
    #words need to be shuffled as list of words will be given at top of
    #document
    shuffle(list_of_words)
    all_example_sentences = ""
    for word in list_of_words:
        all_example_sentences += word_blanked(word) + "\n"

    return(all_example_sentences)
