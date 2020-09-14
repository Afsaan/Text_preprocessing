#importing important libraries
import nltk
import string
import re
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class text_preprocess():
    def __init__(self):
        self.num_to_word = inflect.engine()
        self.translator = str.maketrans('' , '' , string.punctuation)

    def lower_case(self , text):
        print(text.lower())

    def remove_numbers_from_txt(self , text):
        result = re.sub(r'\d+' , '', text)
        print(result)
        

    def convert_num_to_text(self , text):
        word_list = text.split()
        new_str = []

        for word in word_list:
            if word.isdigit():
                word = self.num_to_word.number_to_words(word)
                new_str.append(word)
            else:
                new_str.append(word)
        temp_str = " ".join(new_str)
        print(temp_str)

    def remove_punctuation(self , text):
        print(text.translate(self.translator))

    def remove_stopwords(self):
        pass

    def stemming(self):
        pass

    def lemmatization(self):
        pass

    def pos_tagging(self):
        pass

    def chunking(self):
        pass

    def name_entity_recognition(self):
        pass

if __name__ == "__main__":
    nltk = text_preprocess()
    # nltk.lower_case('Hello WORLD')
    # nltk.remove_numbers_from_txt('hello 4 world')
    # nltk.convert_num_to_text('you bought 6 candies and 4 are at home')
    nltk.remove_punctuation('hello!!! , world!!!!!')

