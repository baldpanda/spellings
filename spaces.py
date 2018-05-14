from random import sample, randint


def word_space_spec(word, num_spaces):
    """Given a word, this function will replace letters in the word
     with blanks (" _ "). The number of letters is specified by the parameter
     num_spaces and the letters are replaced at random.

     Args:
        word (str): a word for some letters to be replaced by blanks
        num_spaces (int): #letters wanted to be replaced by blanks

    Returns:
        (str): The original word but with num_spaces letters replaced at random
        with " _ "
     """

    leng = len(word)
    replace_char_index = sample(range(0, leng), num_spaces)
    rev_replace_char_index = sorted(replace_char_index, reverse=True)
    alt_word = list(word)
    for i in rev_replace_char_index:
        alt_word[i] = " _ "
    alt_word = "".join(alt_word)
    return alt_word


def six_words_with_spaces(word):
    """Given a word, this function returns the word six times with letters
    replaced by blanks. The first word returned returned has one letter replaced
    by a blank. The second has two replaced by a blank... If the word is less than
    six letters then the word is returned with a random number of blanks between
    1 and the word's length.

    Args:
        word (str): the word wanted to be returned

    Returns:
        (str): six copies of the word concatenated with varying numbers of letters
        replaced by blanks
    """

    word_len = len(word)
    num_space = 1
    statement = ""
    # letters_remain = word_len - num_space
    for i in range(0, 6):
        if word_len - num_space >= 0:
            statement = statement + word_space_spec(word, num_space) + ", "
        else:
            statement = statement + \
                word_space_spec(word, randint(1, word_len)) + ", "
        num_space += 1
    return statement[:-2]


def all_words(list_of_words):
    """Given an list of words, this function returns each word six times with
    varying numbers of letters replaced by blanks (" ")

    Args:
        list_of_words (list): the list of words wanted to be used
    Returns:
        (str): 6 copies of each word in list_of_words with varying
        numbers of letters replaced by blanks according to the six_words_with_spaces()
        function. Each lot of six is outputted on a new line"""
    all_words_fin = ""
    for word in list_of_words:
        all_words_fin = all_words_fin + six_words_with_spaces(word) + "\n"
    return all_words_fin
