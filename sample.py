import pandas as pd

data = pd.read_csv("cleaned_vulgar_words.csv")
print(data.columns)

def load_vulgar_words():
    data = pd.read_csv("cleaned_vulgar_words.csv", header=None)  # No header
    return set(data[0].str.lower())  # Access the first column (index 0) and convert to lowercase
