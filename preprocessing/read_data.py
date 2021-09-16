import pandas as pd
import chardet
from nltk.stem.cistem import Cistem
import numpy as np
import pickle

IMPORT_FILE = "../data/wordfreq.tsv"

with open(IMPORT_FILE, 'rb') as f:
    encodingdetector = chardet.detect(f.read())

df = pd.read_csv(IMPORT_FILE, encoding = encodingdetector['encoding'], sep = '\t', header = None, names = ['term', 'variation', 'tag', 'frequency'], index_col = 0)

stemmer = Cistem()
stemmed_terms = [stemmer.stem(str(el)) for el in df.index]
df['term_stemmed'] = stemmed_terms
unique_stemmed_terms = np.unique(stemmed_terms)
values = []
for el in unique_stemmed_terms:
	value = sum(df[df['term_stemmed'] == el]['frequency'])
	values.append(value)


dictionary = {unique_stemmed_terms[el]:values[el] for el in range(len(unique_stemmed_terms))}

with open('wordfreq.pkl', 'wb') as f:
	pickle.dump(dictionary, f)