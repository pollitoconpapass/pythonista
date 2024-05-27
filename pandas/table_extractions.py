import pandas as pd
import camelot


# === TABLE EXTRACTION FROM A WEBPAGE ===
read_url = pd.read_html("<url_link>")
print(read_url[1])  # -> the first table of the url


# === EXTRACT TABLE FROM PDF ===
tables = camelot.read_pdf("path/to/file.pdf", pages="all")  # -> if you want a specific page: pages="1"
print(tables)