import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt') # Download the required tokenizer

df['tokens'] = df['sentence'].apply(word_tokenize)  # replace 'text_column' with the relevant column name

print(df[['sentence', 'tokens']].head()) # Display the original text and its tokenized version
