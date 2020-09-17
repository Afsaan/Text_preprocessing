from textblob import TextBlob , Word


class Text_blob:
    
    def pos_tag(self, text):
        blob = TextBlob(text)
        print(blob.tags)

    def noun_phrase_extraction(self, text):
        blob = TextBlob(text)
        print(blob.noun_phrases)

    def sentiment_analysis(self, text):
        blob = TextBlob(text)
        print(blob.sentiment)

    def tokenize(self, text):
        blob = TextBlob(text)
        print(blob.words)

        print(blob.sentences)

    def lemmatization(self, text):
        blob = TextBlob(text)
        word = blob.words

        print(word[0].singularize())
        print(word[0].pluralize())
        print(word[0].lemmatize())
    
    def synonym_set(self, text):
        word = Word(text)
        print(word.synsets)

    def meaning_of_word(self , text):
        word = Word(text)
        print(word.definitions)




if __name__ == '__main__':
    blob = Text_blob()
    # blob.pos_tag('hello this is Virat Kholi here')
    # blob.noun_phrase_extraction('hello this is Virat Kholi here')
    # blob.tokenize('you are very very good')
    # blob.lemmatization('you are very very good')
    blob.meaning_of_word('computer')


