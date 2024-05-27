import sqlite3
import pandas as pd
import zipfile
import os

# Path to your .apkg file
apkg_file_path = './Quechua_mdico_CMP.apkg'
extracted_path = './extracted_apkg'

# Create a directory to extract the contents
os.makedirs(extracted_path, exist_ok=True)

# Extract the contents of the APKG file
with zipfile.ZipFile(apkg_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_path)

# Path to the extracted SQLite database
db_file_path = os.path.join(extracted_path, 'collection.anki2')

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Query to get the notes
query = """
SELECT n.id, flds
FROM notes n
"""

# Execute the query and fetch the results
cursor.execute(query)
notes = cursor.fetchall()

# Close the connection
conn.close()

# Process the fetched data
data = []
for note in notes:
    fields = note[1].split('\x1f')  # Fields are separated by ASCII unit separator (0x1F)
    data.append(fields)

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Spanish', 'Quechua'])  # Adjust column names as needed
df.to_csv('extracted_data.csv', index=False)
