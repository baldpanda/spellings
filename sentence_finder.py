"""
TO DO:
    * build in coping mechanism for words required that have a capitilised letter
    or punctuation immediatley after (implemented possible solution
    but needs testing)
    * multiple occurreces of the choosen word in the same sentence (just blanks
    first at the moment)
    * if the word of interest is the last word in the sentence, it returns the
    sentence with the word blanked but the punctuation is removed from the end
    of the sentence (implemented possible solution but needs testing)
"""

import os

#sentences.txt is a text file containing all of the current sentences
data_path = os.path.join(os.getcwd(), 'sentences.txt')

def word_in_sent(word):
    """For a given word, this function checks if it is in the text file
    sentences.txt. If it is, then it returns the first instance of that
    sentence. If it is not, it asks the user to input a sentence with that
    word in. This sentence is added to the text file and is also returned.

    Args:
        word (str): the word wanted for example sentences

    Returns:
        (str): an example sentence with the input word in.
    """
    searchfile = open(data_path, "r+")
    sentence = ""
    for line in searchfile:
        sent_norm_list = sentence_normaliser(line)
        poss_sent = " ".join(sent_norm_list)
        if word in poss_sent:
            sentence = line
            break
    if not sentence:
        #if the word is not in the sentence, get the user to input a sentence
        #with the word in
        sentence = input('Please give a sentence with the word {} in: '.format(word))
        searchfile.write("\n" + sentence)
    searchfile.close()
    return(sentence)


def word_blanked(word):
    """ Given a word, this calls the word_in_sent function to provide
    an example of a sentence with that word in. It then replaces the word
    in the sentence with blanks equal to the number of letters of that word
    and returns the updated sentence.

    Args:
        word (str): the required word

    Returns:
        (str): an example sentence with the input word in, but the input word
        is replaced by blanks
    """
    sentence = word_in_sent(word)
    sentence = add_space_before_punct(sentence, [",", ".", "!", "?"])
    sentence_list = sentence.split(" ")
    sent_list_norm = sentence_normaliser(sentence)
    word_loc = sent_list_norm.index(word)
    leng = len(word)
    sentence_list[word_loc] = blanks(leng)
    updated_sentence = " ".join(sentence_list)
    updated_sentence = remove_space_before_punct(updated_sentence, [",", ".", "!", "?"])
    return(updated_sentence)

def blanks(len_of_word):
    """ Gives a string of underscores with spaces between (blanks)
    with the number of underscores equal to the integer input

    Args:
        len_of_word (int): the number of underscores required

    Returns:
        (str): underscores with a space between, where the number of underscores
        equals the len_of_word integer input
    """
    if len_of_word == 1:
        a = "_"
    else:
        a = "_"
        for i in range(0, len_of_word - 1):
            a += " _"
    return(a)


def sentence_normaliser(sentence):
    sent_norm = sentence.replace("\n", "")
    sent_norm = sent_norm.split(" ")
    sent_norm[0] = sent_norm[0].lower()
    sent_len = len(sent_norm)
    return(sent_norm)

def add_space_before_punct(sent, list_of_punct):
    """Adds space before each item of punctuation in the input list.

    Args:
        sent (str): sentence in which the punctuation is released
        list_of_punct (list): list containing punctuation for space to be added
        before

    Returns:
        (str): input sentence but with space added before the punctuation
        given in the list
    """
    sentence = sent
    for punct in list_of_punct:
        sentence = sentence.replace(punct, " " + punct)
    return(sentence)

def remove_space_before_punct(sent, list_of_punct):
    """Removes space before punctuation given in list. Opposite of
    add_space_before_punct
    """
    sentence = sent
    for punct in list_of_punct:
        sentence = sentence.replace(" " + punct, punct)
    return(sentence)
