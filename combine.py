import sentence_finder as sf
import spaces

def comb_funct(list_of_words):
    """Given a list of words, it will return an example sentence for each
    word with the target word blanked out. Below this the function will
    print 6 copies of each word, each with a varying number of letters replaced
    by blanks

    Args:
        list_of_words (list): list of words to populate output

    Returns:
        (str): An example sentence for each word with the word blanked out.
        Below this 6 copies of each word, with a varying number of letters words
        blanked out.
    """
    doc = ""
    doc += sf.example_sentence_mult(list_of_words)
    doc += spaces.all_words(list_of_words)
    return(doc)

print(comb_funct(["across", "sun", "hot", "better", "best", "than", "end", "looking", "there"]))
