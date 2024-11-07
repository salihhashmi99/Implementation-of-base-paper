import re

# Define a function to clean each token in the tokenized list
def clean_tokens(tokens):
    # Remove special characters and numbers, and convert each token to lowercase
    cleaned_tokens = [re.sub(r'[^A-Za-z]', '', token).lower() for token in tokens if re.sub(r'[^A-Za-z]', '', token)]
    return cleaned_tokens

# Apply data cleaning to each list of tokens in the 'tokens' column
df['cleaned_tokens'] = df['tokens'].apply(clean_tokens)

print(df[['tokens', 'cleaned_tokens']].head()) # Display the original tokens and cleaned tokens
