import pandas as pd


existing_df = pd.read_csv("data.csv")

lang1_words = []
lang2_words = []

for i in existing_df["Language 1"]:
    lang1_words.append(i)

for i in existing_df["Language 2"]:
    lang2_words.append(i)

print(len(lang1_words), len(lang2_words))
'''If they are the same, we could make a Hugging Face Dataset as well...'''