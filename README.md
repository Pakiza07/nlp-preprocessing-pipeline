# NLP Preprocessing Pipelines (NLTK & spaCy)

This repository contains a simple introduction to text preprocessing using two popular NLP libraries: **NLTK** and **spaCy**. 
It demonstrates the foundational steps in preparing raw text for natural language processing tasks.

## Features

### Preprocessing Techniques Covered
- Tokenization (sentence and word level)
- Lowercasing
- Punctuation removal
- Stopword removal
- Stemming (PorterStemmer)
- Lemmatization (WordNetLemmatizer with POS tags)
- spaCy-based pipeline (lemmatization + stopword/punctuation removal)

### Libraries Used
- `nltk`
- `spacy`
- `string` (for punctuation removal)

## Files

- `nltk_tut.py`: Demonstrates preprocessing using **NLTK** and **Spacy**

## How to Use

1. Clone the repository  
2. Install required libraries:
   ```bash  
    pip install nltk spacy
    python -m spacy download en_core_web_sm
3.Run the script:
   ```bash
    python nltk_tut.py
