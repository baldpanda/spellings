import os
from random import shuffle
import mult_words_blanks as mwb
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



    # def word_in_sent(word):
    #     searchfile = open(data_path, "r+")
    #     sentence = ""
    #     for line in searchfile:
    #         sent_norm_list = sentence_normaliser(line)
    #         poss_sent = " ".join(sent_norm_list)
    #         if word in add_space_before_punct(poss_sent, [",", ".", "!", "."]).split(" "):
    #             sentence = line
    #             break
    #     if not sentence:
    #         sentence = input('Please give a sentence with the word {} in: '.format(word))
    #         searchfile.write("\n" + sentence)
    #     searchfile.close()
    #     return(sentence.strip("\n"))
#abc = Example_sentence()

# def word_blanked(word):
#     """ Given a word, this calls the word_in_sent function to provide
#     an example of a sentence with that word in. It then replaces the word
#     in the sentence with blanks equal to the number of letters of that word
#     and returns the updated sentence.
#
#     Args:
#         word (str): the required word
#
#     Returns:
#         (str): an example sentence with the input word in, but the input word
#         is replaced by blanks
#     """
#     sentence = word_in_sent(word)
#     sentence = add_space_before_punct(sentence, [",", ".", "!", "?"])
#     sentence_list = sentence.split(" ")
#     sent_list_norm = sentence_normaliser(sentence)
#     word_loc = sent_list_norm.index(word)
#     leng = len(word)
#     if "'" in word:
#         apost_loc = word.index("'")
#         sentence_list[word_loc] = blanks(apost_loc) + "'" + blanks((leng - apost_loc - 1))
#     else:
#         sentence_list[word_loc] = blanks(leng)
#     updated_sentence = " ".join(sentence_list)
#     updated_sentence = remove_space_before_punct(updated_sentence, [",", ".", "!", "?"])
#     return(updated_sentence)
#
#
# def example_sentence_mult(list_of_words):
#     """Takes a list of words and returns an example sentence for each.
#     For each of these sentences the target word is blanked out.
#
#     Args:
#         list_of_words (list): list of the words wanted for example sentences
#
#     Returns:
#         (str): Example sentences for each word in the input, with each
#         new sentence on a new line
#     """
#     #words need to be shuffled as list of words will be given at top of
#     #document
#     shuffle(list_of_words)
#     all_example_sentences = ""
#     for word in list_of_words:
#         all_example_sentences += word_blanked(word) + "\n"
#
#     return(all_example_sentences)
