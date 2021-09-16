import pickle
import pandas as pd
import chardet
import re
import numpy as np
from nltk.stem.cistem import Cistem
from statistics import mean

stemmer = Cistem()

with open('../preprocessing/wordfreq.pkl', 'rb') as f:
	dereko = pickle.load(f)

INPUT = "../data/input.xlsx"

#with open(IMPORT_FILE, 'rb') as f:
#    encodingdetector = chardet.detect(f.read())

df = pd.read_excel(INPUT)

df['id'] = [str(df['Title'][el]) + ' by ' + str(df['Artist'][el]) for el in range(len(df['Title']))]

EXISTING = 'results.xlsx'

existingdf = pd.read_excel(EXISTING)

def tokenise(text):
	text = re.sub('[^a-zA-ZäöüÄÖÜß]'," ", str(text))
	tokens = text.lower().split()
	tokens_stemmed = [stemmer.stem(el) for el in tokens]
	return tokens_stemmed

def score_text(songid):
	text = df[df['id'] == songid]['Lyrics'].values[0]
	tokens = tokenise(text)
	unique_tokens = np.unique(tokens)
	values = []
	for el in unique_tokens:
		try:
			value = dereko[el]
		except:
			value = 0
		values.append(value)
	return mean(values)

existing_songs = set(existingdf['Song'])

for el in df['id']:
	if el not in existing_songs:
		score = score_text(el)
		existingdf.loc[len(existingdf.index)] = [el, score]

existingdf.to_excel(EXISTING, index = False)



