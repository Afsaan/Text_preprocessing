# Text_preprocessing

### Text lowercase
We do lowercase the text to reduce the size of the vocabulary of our text data.

### Remove numbers
We should either remove the numbers or convert those numbers into textual representations.
We use regular expressions(re) to remove the numbers.

### Remove Punctuation
We remove punctuations because of that we don't have different form of the same word. If we don't remove punctuations, then been, been, and been! will be treated separately.

### Remove default stopwords:
Stopwords are words that do not contribute to the meaning of the sentence. Hence, they can be safely removed without causing any change in the meaning of a sentence. The NLTK(Natural Language Toolkit) library has the set of stopwords and we can use these to remove stopwords from our text and return a list of word tokens.

### Stemming
From Stemming we will process of getting the root form of a word. Root or Stem is the part to which inflextional affixes(like -ed, -ize, etc) are added. We would create the stem words by removing the prefix of suffix of a word. So, stemming a word may not result in actual words.


### Lemmatization
As stemming, lemmatization do the same but the only difference is that lemmatization ensures that root word belongs to the language. Because of the use of lemmatization we will get the valid words. In NLTK(Natural language Toolkit), we use WordLemmatizer to get the lemmas of words. We also need to provide a context for the lemmatization.So, we added pos(parts-of-speech) as a parameter. 

### Parts of Speech (POS) Tagging
The pos(parts of speech) explain you how a word is used in a sentence. In the sentence, a word have different contexts and semantic meanings. The basic natural language processing(NLP) models like bag-of-words(bow) fails to identify these relation between the words. For that we use pos tagging to mark a word to its pos tag based on its context in the data. Pos is also used to extract rlationship between the words. 

### Named Entity Recognition
It is used to extract information from unstructured text. It is used to classy the entities which is present in the text into categories like a person, organization, event, places, etc. This will give you a detail knowledge about the text and the relationship between the different entities.