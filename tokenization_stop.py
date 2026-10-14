
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = "This is a good product and it is very useful."

# Tokenization
tokens = word_tokenize(text)
print("Original tokens:", tokens)

# Remove stopwords
stop_words = set(stopwords.words("english"))

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("After removing stopwords:", filtered_words)
