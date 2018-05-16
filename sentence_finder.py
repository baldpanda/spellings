"""
TO DO:
    * build in coping mechanism for words required that have a capitilised letter
    or punctuation immediatley after 
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
        if word in line:
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
    sentence_list = sentence.split(" ")
    word_loc = sentence_list.index(word)
    leng = len(word)
    sentence_list[word_loc] = blanks(leng)
    updated_sentence = " ".join(sentence_list)
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
