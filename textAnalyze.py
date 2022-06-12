# This file contains logic for text simplification in order to reduce index size

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from nltk.probability import FreqDist

PT_STOPWORDS = stopwords.words('portuguese')

stemmer = RSLPStemmer()


def reduce_analyze_text(text):
    tokenized_text = word_tokenize(text, language='portuguese')

    # Drop small words and stopwords
    filtered_text = [
        word.lower() for word in tokenized_text if ((word.lower() not in PT_STOPWORDS) and (len(word) > 2))]

    # Stemming
    stemmed_text = [stemmer.stem(word) for word in filtered_text]

    # Get term frequency pair
    # TODO: change frequency to integer
    f_dist = FreqDist(stemmed_text)

    return [(word, f_dist.freq(word)) for word in stemmed_text]
