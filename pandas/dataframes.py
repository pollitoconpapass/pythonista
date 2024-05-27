import pandas as pd


# === CREATE A DATAFRAME ===
data_summary = {
    "Metrics": ["B1", "B2", "B3"],
    "Values": [100, 200, 300]
}

df = pd.DataFrame(data_summary)


# === TO KNOW THE AMOUNT OF CELLS IN AN EXCEL/CSV FILE ===
df_excel = pd.read_excel("path/to/file.xlsx")
total_cells = df_excel.shape[0]


# === IDENTIFY THE COLUMNS OF A DF ===
columns = pd.read_excel("path/to/file.xlsx").columns
print(columns)


# === SELECT A SPECIFIC COLUMN ===
selected_column = df["column_name"]  # -> df already pre-initiated
