from gensim.models import Word2Vec

# Train Word2Vec model on the tokenized data
word2vec_model = Word2Vec(sentences=df['lemmatized_tokens'], vector_size=100, window=5, min_count=1, workers=4)

# To get the vector for a word, e.g., 'requirement'
print("Vector for 'requirement':", word2vec_model.wv['requirement'])

# Aggregate vectors to represent each document
df['word2vec_vectors'] = df['lemmatized_tokens'].apply(lambda tokens: sum(word2vec_model.wv[token] for token in tokens if token in word2vec_model.wv))
