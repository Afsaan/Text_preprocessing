#importing important libraries
import nltk
import string
import re


class text_preprocess():
    def __init__(self):
        pass

    def lower_case(self , text):
        print(text.lower())

    def remove_numbers_from_txt(self , text):
        result = re.sub(r'\d+' , '', text)
        print(result)
        

    def convert_num_to_text(self):
        pass

    def remove_punctuation(self):
        pass

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
    nltk.lower_case('Hello WORLD')
    nltk.remove_numbers_from_txt('hello 4 world')

