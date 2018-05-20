import sentence_finder as sf
import spaces
import datetime

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
    doc = "This weeks spellings are: "
    for word in list_of_words:
        doc += word + ", "
    doc = doc[:-2]
    doc += ":\n\n"
    doc += sf.example_sentence_mult(list_of_words) + "\n"
    doc += spaces.all_words(list_of_words)

    #create a text file to put doc into
    curr_date = str(datetime.datetime.now()).replace(".", "_").replace(" ", "_").replace(":", "_")
    file_name = "spellings_" + curr_date + ".txt"
    f = open(file_name, "w+")
    f.write((doc))
    f.close()
