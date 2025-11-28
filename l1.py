import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
text = '''NLTK is a leading platform for building Python programs to work with human language data. 
        It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, 
        along with a suite of text processing libraries for classification, tokenization, stemming, 
        tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, 
        and an active discussion forum.'''
sentences = sent_tokenize(text)
print("----- SENTENCE TOKENIZATION -----")
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")
sample_text = "I won’t go to the party because I don’t feel well."
words = word_tokenize(sample_text)
print("\n----- WORD TOKENIZATION -----")
print(f"Original Text: {sample_text}")
print("Tokens:", words)
