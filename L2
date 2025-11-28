import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
import string
nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))
def remove_stopwords(text):
    words = word_tokenize(text)
    filtered_words = [
        word for word in words 
        if word.lower() not in english_stopwords and word not in string.punctuation
    ]
    filtered_text = ' '.join(filtered_words)
    return filtered_text
text = "NLTK is a leading platform for building Python programs to work with human language data."
filtered_text = remove_stopwords(text)
print(filtered_text)
