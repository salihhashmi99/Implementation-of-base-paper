from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') #Load the tokenizer
model = BertModel.from_pretrained('bert-base-uncased') #Load the pre-trained BERT

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device) # Move model to GPU if available, else stay on CPU

# Function to extract BERT embeddings for each sentence
def get_bert_embeddings(text):
    # Tokenize the sentence with padding and truncation (handles varying sentence lengths)
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Get the model outputs (outputs[0] is the last hidden state)
    with torch.no_grad():  # Disable gradient calculation as we're not training
        outputs = model(**inputs)

    # We use the [CLS] token (first token in BERT) as the sentence embedding
    sentence_embedding = outputs.last_hidden_state[:, 0, :].cpu().numpy()  # Move back to CPU and convert to numpy
    return sentence_embedding

# Apply BERT embeddings to each sentence
# Use 'lemmatized_tokens' or the correct column name where your cleaned text resides
df['bert_embeddings'] = df['lemmatized_tokens'].apply(lambda x: get_bert_embeddings(' '.join(x)))

# Check the shape of the resulting embeddings
print(f"BERT Embeddings Shape: {df['bert_embeddings'].iloc[0].shape}")
