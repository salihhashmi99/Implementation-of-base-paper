from sklearn.feature_extraction.text import CountVectorizer

# Convert preprocessed text into a format suitable for vectorization
preprocessed_text = df['lemmatized_tokens'].apply(lambda x: ' '.join(x))

tf_vectorizer = CountVectorizer() # Initialize CountVectorizer to compute TF
tf_matrix = tf_vectorizer.fit_transform(preprocessed_text)

# Display TF feature matrix
print("TF Matrix Shape:", tf_matrix.shape)
print("Sample TF Matrix:", tf_matrix.toarray())
