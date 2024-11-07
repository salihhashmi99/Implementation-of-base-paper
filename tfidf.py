from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer() # Initialize TfidfVectorizer to compute TF-IDF
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_text)

# Display TF-IDF feature matrix
print("TF-IDF Matrix Shape:", tfidf_matrix.shape)
print("Sample TF-IDF Matrix:", tfidf_matrix.toarray())
