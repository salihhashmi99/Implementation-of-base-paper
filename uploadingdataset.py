import pandas as pd
from google.colab import files
uploaded = files.upload() # This opens a dialog to upload files manually

dataset_path = 'Pure_Annotate_Dataset.csv'
try:
    df = pd.read_csv(dataset_path, encoding='ISO-8859-1')
except UnicodeDecodeError:
    # If ISO-8859-1 doesn't work, you can try 'latin1' or 'utf-16'
    df = pd.read_csv(dataset_path, encoding='latin1')

# Display a success message and preview the dataset
print("Dataset Loaded Successfully")
print(df.head())
print("\nDataset Information:")
df.info()
