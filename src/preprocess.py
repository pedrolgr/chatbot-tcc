import spacy
import re
from unidecode import unidecode

nlp = spacy.load('pt_core_news_sm')

def preprocess(sentence):
    text_cleaned = re.sub(r'[^\w\s]', '', sentence.lower())
    processed_words = []
    doc = nlp(text_cleaned)
    for token in doc:
        token_lemmatized = token.lemma_
        token_no_acennts = unidecode(token_lemmatized)
        processed_words.append(token_no_acennts)


    return ' '.join(processed_words)

