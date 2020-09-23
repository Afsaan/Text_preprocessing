import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
class Spacy():

    def tokenization(self , text):
        doc = nlp(text)
        for token in doc:
            print(token.text, token.pos_ , token.dep_)

    def part_of_Speech(self,text):
        doc = nlp(text)
        for token in doc:
            print(token.text, token.lemma_ , token.pos_ , token.tag_, token.shape_, token.is_alpha, token.is_stop)

    def dispay_dependencies(self, text):
        doc = nlp(text)
        displacy.serve(doc , style = 'dep') #dep means dependency

    def entities(self, text):
        doc = nlp(text)
        for ent in doc.ents:
            print(ent.text , ent.start_char, ent.end_char, ent.label_)

    def dispay_dependencies(self, text):
        doc = nlp(text)
        displacy.serve(doc , style = 'ent') #dep means dependency


if __name__ == '__main__':
    obj = Spacy()
    # obj.tokenization('Apple is looking at buying U.K. startup for $1 million')
    # obj.part_of_Speech('Apple is looking at buying U.K. startup for $1 million')
    # obj.dispay('Apple is looking at buying U.K. startup for $1 million')
    # obj.dispay('Apple is looking at buying U.K. startup for $1 million')
    obj.entities('Apple is looking at buying U.K. startup for $1 million')
    

