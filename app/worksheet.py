import datetime
import mult_words_blanks as mwb
import example_sentence as es

class Worksheet:

    def __init__(self):
        worksheets_directory = "worksheets" + "/"
        curr_date = str(datetime.datetime.now()).replace(".", "_").replace(" ", "_").replace(":", "_")
        self.introduction = ""
        self.words_with_blanks = ""
        self.sentences = ""
        self.name = worksheets_directory + "spellings_" + curr_date + ".txt"

    def generate_introduction(self, list_of_words):
        self.introduction = "This weeks spellings are: "
        for word in list_of_words:
            self.introduction += word + ", "
        self.introduction = self.introduction[:-2]

    def generate_words_with_blanks(self, list_of_words):
        all_words = mwb.All_words()
        self.words_with_blanks = all_words.generate_all_words(list_of_words)

    def generate_sentences(self, list_of_words):
        sentences = es.Example_sentence("")
        self.sentences = sentences.generate_mult_sentences_with_blanks(list_of_words)

    def write_to_text_file(self, list_of_words):
        self.generate_introduction(list_of_words)
        self.generate_words_with_blanks(list_of_words)
        self.generate_sentences(list_of_words)

        text_for_sheet = self.introduction + "\n\n" + self.words_with_blanks + "\n" + self.sentences
        file = open(self.name, "w+")
        file.write((text_for_sheet))
        file.close()

example_worksheet = Worksheet()
print(example_worksheet.write_to_text_file(["tree", "cat", "hamster"]))

    # def main():
    #     example_worksheet = Worksheet()
    #     list_of_words = input('Please enter a list of words: '.format(word))
    #     example_worksheet.generate_introduction(list_of_words)
    #     example_worksheet.generate_words_with_blanks(list_of_words)
    #     example_worksheet.generate_sentences(list_of_words)
    #     text_for_sheet = example_worksheet.introduction + "\n\n" + example_worksheet.words_with_blanks + "\n" + example_worksheet.sentences
    #     example_sentence.write_to_text_file(text_for_sheet)
    #
    # if __name__ == "__main__":
    #     main()
