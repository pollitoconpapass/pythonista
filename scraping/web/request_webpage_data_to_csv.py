import requests
import pandas as pd


url = "http://urlofSentences"
url_2 = "http://urlofSentences2"

url_data = requests.get(url).text.split("\n")
url_data2 = requests.get(url_2).text.split("\n")

df = pd.DataFrame({
    "Language 1": url_data,
    "Language 2": url_data2
})

df.to_csv("sentences.csv", index=False) # -> for avoiding the 0, 1, 2...
