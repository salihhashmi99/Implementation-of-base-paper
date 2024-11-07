from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4') # Download WordNet data for lemmatization (run once)

lemmatizer = WordNetLemmatizer() # Initialize the lemmatizer

# Define a function
def lemmatize_tokens(tokens):
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens #lemmatize each token in the cleaned tokens list

# Apply lemmatization to each list of cleaned tokens
df['lemmatized_tokens'] = df['cleaned_tokens'].apply(lemmatize_tokens)

# Display the original, cleaned, and lemmatized tokens
print(df[['tokens', 'cleaned_tokens', 'lemmatized_tokens']].head())
