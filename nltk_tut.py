import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import spacy

example_text = "Hello there! How are you doing today? I hope you're having a great day."
print(sent_tokenize(example_text))
print(word_tokenize(example_text))
for i in word_tokenize(example_text):
    print(i)

example_sentence = "This is an example sentence demonstrating stopwords filtration."
stop_words = set(stopwords.words("english"))

words= word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

# The code above demonstrates basic text processing using NLTK, including tokenization and stopword removal.
# filtered_sentence = [w for w in words if not w in stop_words ]  # This is a more concise way to filter stopwords.

ps = PorterStemmer()

example_words =["python", "pythoner", "pythoning", "pythonly"]

for w in example_words:
    print(ps.stem(w))

# The code above demonstrates stemming using the Porter Stemmer from NLTK.
# Stemming is the process of reducing words to their root form.

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoneres have pythoned poorly at some point."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))


# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Helper function to convert POS tags to WordNet format
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun

# Example sentence
sentence = "The striped bats are hanging on their feet for best"

# Tokenize and tag parts of speech
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

# Lemmatize with POS tags
lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]

# Display results
print("Original:", sentence)
print("Lemmatized:", " ".join(lemmatized))

# The code above demonstrates lemmatization using the WordNetLemmatizer from NLTK.
# Lemmatization is the process of reducing words to their base or dictionary form, considering their part of speech.
# The code also includes a helper function to convert POS tags from the Penn Treebank format to WordNet format.


nltk.download('punkt')

text = "Tomorrow, I'll start learning NLP! It's going to be amazing :)"
text = text.lower()
tokens = word_tokenize(text)
cleaned = [
    word for word in tokens
    if word not in string.punctuation and word not in stopwords.words('english')
]
print(cleaned)

# The code above demonstrates basic text preprocessing techniques such as tokenization, lowercasing, and punctuation removal.

nlp = spacy.load("en_core_web_sm")
doc = nlp("Tomorrow, I'll start learning NLP! It's going to be amazing :)")
cleaned = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
print(cleaned)
# The code above demonstrates text preprocessing using spaCy, including lemmatization and stopword removal.







